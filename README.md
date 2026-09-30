# Vision Based Autonomous Navigation for Unmanned Ground Vehicle for Outdoor Environment

## 🚙 INNOPATH — What We Are Building

**SIH26126 Project**: Vision-Based Autonomous Navigation for an Outdoor UGV

### System Architecture Overview

```
                 CAMERA
                    │
                    ▼
          ┌──────────────────┐
          │  AI PERCEPTION   │
          │                  │
          │ Terrain +        │
          │ Obstacles        │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ VISUAL ODOMETRY  │
          │ / VISUAL SLAM    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │  PATH PLANNER    │
          │                  │
          │ Safe path        │
          │ Point A → B      │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ MOTOR COMMANDS   │
          └────────┬─────────┘
                   │
                   ▼
                  UGV
```

---

## 🧠 Phase 1 — Perception AI

The camera provides real-time vision processed into semantic understanding:

```
RGB Image ──► AI Model ──► Semantic Understanding ──► Terrain + Obstacles
```

The model learns semantic scene classes (grass, mud, puddle, tree, bush, rubble, fence, vehicle, person, etc.) and maps them into navigation affordances:

- **SAFE / TRAVERSABLE**: Grass, smooth terrain, suitable ground
- **CAUTION**: Mud, puddles, difficult/uneven terrain
- **BLOCKED / OBSTACLE**: Trees, fences, vehicles, persons, rubble, barriers

> *Note: Navigation categories are dynamically refined through experimental validation rather than assumed statically.*

---

## 📦 Phase 2 — Datasets

1. **RELLIS-3D** (Primary Off-Road Perception Dataset):
   - 13,556 camera images ✅
   - 6,234 labeled images ✅
   - Image/label matching ✅
   - Mask verification ✅
   - Class ID inspection ✅
   - Class distribution analysis ✅
   *(Labels include: grass, tree, sky, bush, puddle, mud, rubble, fence, vehicle, person, etc.)*

2. **The Great Outdoors** (Environmental Diversity & Generalization):
   - Adds diverse outdoor terrain, varying vegetation, lighting conditions, and off-road scenarios to prevent overfitting.
   - Targeted download: focused exclusively on required visual/semantic assets (excluding heavy LiDAR/radar/ROS bags).

3. **KITTI** (Localization & Odometry Evaluation):
   - Benchmark dataset utilized for Visual Odometry and SLAM pipeline evaluation.

---

## 🏋️ Phase 3 — Train the Perception Model

```
Training Images + Ground-Truth Masks ──► Neural Network ──► Predictions 
       ▲                                                           │
       └────────────── Backpropagation & Loss ◄────────────────────┘
```

- **Hardware**: NVIDIA GeForce RTX 4060
- **Target Metrics**: mIoU, class IoU, precision/recall, validation loss, inference FPS, latency, and model footprint.
- **Priority**: High segmentation fidelity paired with low-latency inference for real-time robotic control.

---

## 🌦️ Phase 4 — Generalization

Evaluating model robustness outside the training distribution:
- Diverse terrains and lighting variations
- Muddy, unstructured, and novel outdoor environments
- Custom recorded field video testing

```
              TRAIN
     (RELLIS + Great Outdoors)
                 │
                 ▼
               MODEL
                 │
                 ▼
       TEST ON UNSEEN DATA
          ┌──────┴──────┐
          ▼             ▼
      Known-ish      New Environment
```

---

## ⚡ Phase 5 — Lightweight Model

- Exploring efficient backbones and architectures (referencing **MobileNetV3**).
- Optimizing accuracy vs. speed vs. hardware resource consumption for onboard deployment.

---

## 🗺️ Phase 6 — Visual Odometry / SLAM

Estimates ego-motion across successive frames to determine relative localization:

```
Frame 1 ──► Frame 2 ──► Frame 3 ──► Frame 4
   │           │           │           │
   └───────────┴─────┬─────┴───────────┘
                     ▼
           Camera Motion Estimation
                     ▼
             Relative Position
                     ▼
                 Local Map
```
- Reference baseline: **ORB-SLAM3**

---

## 🧭 Phase 7 — Path Planning

Integrates perception and localization to compute safe navigation waypoints:

```
        TREE
         █
         █
START ● ────────╮
                │
             GRASS
                │
        █████   │
        MUD     │
                ╰────── ● GOAL
```

- **Inputs**: Terrain map + Obstacle map + UGV pose + Target Goal
- **Outputs**: Path trajectory / directional velocity commands

---

## 🤖 Phase 8 — Physical UGV Integration

```
Camera ──► Laptop / Edge Computer (INNOPATH AI: Perception, SLAM, Planner)
                  │
                  ▼
         Motor Controller (e.g., ESP32 / MCU)
                  │
                  ▼
                 UGV
```

---

## 🧪 Phase 9 — Real-World Testing & Benchmarking

- Video and simulation evaluation
- Real-time closed-loop testing on physical UGV
- Quantitative metrics: navigation success rate, collision avoidance, FPS, localization drift, failure mode analysis.

---

## 📊 Final INNOPATH System

```
                    INNOPATH
                       │
             ┌─────────┴─────────┐
             │                   │
          PERCEPTION          LOCALIZATION
             │                   │
       Terrain/Obstacle     Visual Odometry
             │              / SLAM
             │                   │
             └─────────┬─────────┘
                       │
                       ▼
                 WORLD MODEL
                       │
                       ▼
                 PATH PLANNER
                       │
                       ▼
                 MOTOR CONTROL
                       │
                       ▼
                      UGV
```

---

## 📍 Current Project Status

```
Dataset acquisition
       ↓
RELLIS inspection       ✅
       ↓
Image/label matching    ✅
       ↓
Label verification      ✅
       ↓
Class distribution      ✅
       ↓
Great Outdoors          🔵 WE ARE HERE
       ↓
Dataset preparation
       ↓
Perception training
       ↓
Evaluation
       ↓
Lightweight optimization
       ↓
Visual odometry / SLAM
       ↓
Path planning
       ↓
UGV integration
       ↓
Real-world testing
```

---

## 📁 Repository Structure

```
├── check all label.py                      # Batch label verification
├── checking label and image.py             # Image and label alignment check
├── vaildation of image and label match.py  # Strict match validator
├── vaildation of label and image id.py     # Class ID inspection
├── view_pair.py                            # Interactive pair visualizer
├── UGV_SIH26126_Idea_PPT.pptx              # Concept presentation
├── 1905.02244v5.pdf                        # Reference paper
├── 2007.11898v2.pdf                        # Reference paper
├── 2011.12954v4.pdf                        # Reference paper
├── geiger_et_al_cvpr12.pdf                 # Reference paper
├── .gitignore                              # Excludes heavy dataset files (~12GB)
└── README.md                               # Project documentation & roadmap
```
