# INNOPATH 🚙
## Vision-Based Autonomous Navigation for Outdoor UGVs

<p align="center">
  <b>AI-Powered Perception • Visual Localization • Traversability • Autonomous Navigation</b>
</p>

---

## 📌 Overview

**INNOPATH** is a vision-based autonomous navigation system designed for **Unmanned Ground Vehicles (UGVs) operating in outdoor and GPS-denied environments**.

The system uses a camera as the primary perception sensor to understand the surrounding environment, identify terrain and obstacles, estimate vehicle movement using visual odometry/SLAM, and generate a safe path from **Point A to Point B**.

The project is being developed for **Smart India Hackathon 2026 – SIH26126: Vision Based Autonomous Navigation for Unmanned Ground Vehicle for Outdoor Environment**.

---

## 🎯 Problem

Outdoor UGVs operate in environments where:

- GPS may be unavailable or unreliable.
- Terrain can be unstructured and unpredictable.
- Lighting and environmental conditions can change.
- Obstacles may not follow predefined road structures.
- The vehicle needs to distinguish traversable terrain from unsafe regions.
- Navigation must operate with limited computational resources.

Traditional navigation approaches can become difficult when the environment does not provide reliable maps, road markings, or GPS localization.

INNOPATH addresses this challenge using a **camera-first AI navigation pipeline**.

---

## 💡 Proposed Solution

INNOPATH combines three major capabilities:

1. **AI-based visual perception**
2. **Visual odometry / SLAM**
3. **Path planning and navigation**

### System Pipeline

```text
                 RGB CAMERA
                     │
                     ▼
          ┌─────────────────────┐
          │   AI PERCEPTION     │
          │                     │
          │ Terrain + Obstacles │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Traversability Map  │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Visual Odometry /   │
          │      Visual SLAM    │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │    PATH PLANNER     │
          │                     │
          │   Point A → Point B │
          └──────────┬──────────┘
                     │
                     ▼
             NAVIGATION COMMAND
                     │
                     ▼
                    UGV
```
