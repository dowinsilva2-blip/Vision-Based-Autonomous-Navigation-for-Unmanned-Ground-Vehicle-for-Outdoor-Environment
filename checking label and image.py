from pathlib import Path

DATASET = Path(r"C:\SIH26126\dataset")

IMAGE_ROOT = DATASET / "Rellis_3D_pylon_camera_node"
LABEL_ROOT = DATASET / "Rellis_3D_pylon_camera_node_label_id"


# --------------------------------------------------
# Find all camera images
# --------------------------------------------------

image_files = list(IMAGE_ROOT.rglob("*.jpg"))


# --------------------------------------------------
# Find all ID labels
# --------------------------------------------------

label_files = list(LABEL_ROOT.rglob("*.png"))


# --------------------------------------------------
# Create dictionaries using filename stem
# --------------------------------------------------

images = {}

for file in image_files:
    images[file.stem] = file


labels = {}

for file in label_files:
    labels[file.stem] = file


# --------------------------------------------------
# Find matching pairs
# --------------------------------------------------

matching_names = set(images.keys()) & set(labels.keys())

missing_labels = set(images.keys()) - set(labels.keys())

missing_images = set(labels.keys()) - set(images.keys())


# --------------------------------------------------
# Print results
# --------------------------------------------------

print("=" * 60)
print("          RELLIS-3D IMAGE/LABEL MATCHING")
print("=" * 60)

print(f"Camera images        : {len(images)}")
print(f"ID labels            : {len(labels)}")
print(f"Matching pairs       : {len(matching_names)}")
print(f"Images without label : {len(missing_labels)}")
print(f"Labels without image : {len(missing_images)}")

print("=" * 60)


# --------------------------------------------------
# Show a few matching examples
# --------------------------------------------------

print("\nFIRST 10 MATCHING PAIRS")
print("=" * 60)

for name in sorted(matching_names)[:10]:

    print("\nIMAGE:")
    print(images[name])

    print("LABEL:")
    print(labels[name])


# --------------------------------------------------
# Show a few unmatched images
# --------------------------------------------------

print("\n\nFIRST 10 IMAGES WITHOUT LABEL")
print("=" * 60)

for name in sorted(missing_labels)[:10]:
    print(images[name])