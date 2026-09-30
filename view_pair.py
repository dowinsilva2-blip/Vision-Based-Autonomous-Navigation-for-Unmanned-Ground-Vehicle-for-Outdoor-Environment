from pathlib import Path
import cv2
import matplotlib.pyplot as plt


# ==========================================
# DATASET PATHS
# ==========================================

DATASET = Path(r"C:\SIH26126\dataset")

IMAGE_ROOT = DATASET / "Rellis_3D_pylon_camera_node"
LABEL_ROOT = DATASET / "Rellis_3D_pylon_camera_node_label_id"


# ==========================================
# FIND ALL IMAGES
# ==========================================

image_files = sorted(IMAGE_ROOT.rglob("*.jpg"))

print("Total camera images:", len(image_files))


# ==========================================
# FIND A REAL IMAGE + LABEL PAIR
# ==========================================

selected_image = None
selected_label = None

for image_path in image_files:

    # Get only the filename without .jpg
    filename = image_path.stem

    # Search for the same filename in label directory
    possible_labels = list(LABEL_ROOT.rglob(filename + ".png"))

    if possible_labels:

        selected_image = image_path
        selected_label = possible_labels[0]
        break


# ==========================================
# CHECK
# ==========================================

if selected_image is None:

    print("ERROR: No matching image/label pair found.")
    exit()


print("\nMATCH FOUND")

print("\nIMAGE:")
print(selected_image)

print("\nLABEL:")
print(selected_label)


# ==========================================
# READ IMAGE
# ==========================================

image = cv2.imread(str(selected_image))

if image is None:
    print("ERROR: Could not read image.")
    exit()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# ==========================================
# READ LABEL
# ==========================================

mask = cv2.imread(
    str(selected_label),
    cv2.IMREAD_UNCHANGED
)

if mask is None:
    print("ERROR: Could not read label.")
    exit()


# ==========================================
# INFORMATION
# ==========================================

print("\nImage shape:")
print(image.shape)

print("\nMask shape:")
print(mask.shape)

print("\nMask data type:")
print(mask.dtype)

print("\nUnique label IDs:")

unique_ids = sorted(set(mask.flatten()))

print(unique_ids)

from collections import Counter

pixel_counts = Counter(mask.flatten())

print("\nPIXEL COUNT PER LABEL ID:")
for label_id, count in sorted(pixel_counts.items()):
    print(f"ID {label_id}: {count} pixels")

# ==========================================
# DISPLAY
# ==========================================

plt.figure(figsize=(14, 6))


plt.subplot(1, 2, 1)

plt.imshow(image)

plt.title("Original Camera Image")

plt.axis("off")


plt.subplot(1, 2, 2)

plt.imshow(mask, cmap="tab20")

plt.title("ID Segmentation Mask")

plt.axis("off")


plt.tight_layout()

plt.show()