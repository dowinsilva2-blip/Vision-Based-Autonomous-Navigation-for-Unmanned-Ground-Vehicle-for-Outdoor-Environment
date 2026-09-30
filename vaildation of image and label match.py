from pathlib import Path
from collections import Counter

DATASET = Path(r"C:\SIH26126\dataset")

IMAGE_ROOT = DATASET / "Rellis_3D_pylon_camera_node"
LABEL_ROOT = DATASET / "Rellis_3D_pylon_camera_node_label_id"

# Find all images
image_files = list(IMAGE_ROOT.rglob("*.jpg"))
image_files += list(IMAGE_ROOT.rglob("*.png"))

# Find all labels
label_files = list(LABEL_ROOT.rglob("*.png"))

print("=" * 60)
print("             RELLIS-3D DATASET CHECK")
print("=" * 60)

print(f"Camera images found : {len(image_files)}")
print(f"ID labels found     : {len(label_files)}")

print("\n" + "=" * 60)
print("IMAGES BY SEQUENCE")
print("=" * 60)

image_sequences = Counter()

for file in image_files:
    relative = file.relative_to(IMAGE_ROOT)

    # First folder after Rellis-3D
    parts = relative.parts

    if len(parts) > 0:
        image_sequences[parts[0]] += 1

for sequence, count in sorted(image_sequences.items()):
    print(f"{sequence}: {count}")

print("\n" + "=" * 60)
print("LABELS BY SEQUENCE")
print("=" * 60)

label_sequences = Counter()

for file in label_files:
    relative = file.relative_to(LABEL_ROOT)

    parts = relative.parts

    if len(parts) > 0:
        label_sequences[parts[0]] += 1

for sequence, count in sorted(label_sequences.items()):
    print(f"{sequence}: {count}")

print("\n" + "=" * 60)