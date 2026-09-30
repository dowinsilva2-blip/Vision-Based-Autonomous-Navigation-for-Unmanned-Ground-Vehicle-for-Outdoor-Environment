from pathlib import Path
from collections import Counter
import cv2

DATASET = Path(r"C:\SIH26126\dataset")

LABEL_ROOT = DATASET / "Rellis_3D_pylon_camera_node_label_id"

label_files = sorted(LABEL_ROOT.rglob("*.png"))

print("Total label images:", len(label_files))

total_counts = Counter()

for i, label_path in enumerate(label_files):

    mask = cv2.imread(str(label_path), cv2.IMREAD_UNCHANGED)

    if mask is None:
        print("Could not read:", label_path)
        continue

    ids, counts = __import__("numpy").unique(mask, return_counts=True)

    for label_id, count in zip(ids, counts):
        total_counts[int(label_id)] += int(count)

    if (i + 1) % 500 == 0:
        print(f"Processed {i + 1}/{len(label_files)}")

print("\n================================")
print("ALL RELLIS LABEL IDs")
print("================================")

for label_id, count in sorted(total_counts.items()):

    print(f"ID {label_id:2d} : {count:,} pixels")