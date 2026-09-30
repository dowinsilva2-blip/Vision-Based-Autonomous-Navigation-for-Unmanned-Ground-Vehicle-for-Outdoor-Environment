from pathlib import Path

# ==============================
# RELLIS-3D DATASET PATHS
# ==============================

DATASET = Path(r"C:\SIH26126\dataset")

IMAGE_ROOT = DATASET / "Rellis_3D_pylon_camera_node"
LABEL_ROOT = DATASET / "Rellis_3D_pylon_camera_node_label_id"


# ==============================
# FIND IMAGE FILES
# ==============================

image_files = list(IMAGE_ROOT.rglob("*.jpg"))

# Some datasets may use PNG images too
image_files += list(IMAGE_ROOT.rglob("*.png"))


# ==============================
# FIND LABEL FILES
# ==============================

label_files = list(LABEL_ROOT.rglob("*.png"))


# ==============================
# PRINT RESULTS
# ==============================

print("=" * 50)
print("       RELLIS-3D DATASET CHECK")
print("=" * 50)

print(f"Camera images found : {len(image_files)}")
print(f"ID labels found     : {len(label_files)}")

print("=" * 50)