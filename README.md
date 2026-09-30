# SIH26126 - UGV Off-Road Perception & Navigation

This repository contains scripts, presentations, and research references for the Smart India Hackathon (SIH26126) project focusing on Unmanned Ground Vehicle (UGV) perception using the Rellis-3D dataset.

## Contents
- **Python Scripts**: Dataset inspection, validation, and visualization utilities for Rellis-3D camera imagery and semantic label annotations.
  - `check all label.py`: Verifies labels across sequences.
  - `checking label and image.py`: Validates image and annotation correspondence.
  - `vaildation of image and label match.py`: Checks exact image-to-label matches.
  - `vaildation of label and image id.py`: Matches label IDs.
  - `view_pair.py`: Visualizes paired camera images and ground-truth segmentation masks.
- **Presentation**: `UGV_SIH26126_Idea_PPT.pptx` outlining the project concept and methodology.
- **Reference Papers**: Included research papers on off-road autonomous navigation and semantic scene understanding.

## Note on Dataset
The Rellis-3D dataset (~12GB) is excluded from version control via `.gitignore`. Place the `dataset/` directory in the project root to run the scripts locally.
