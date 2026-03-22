# Gesture Controlled Robotic Hand

A gesture-controlled robotic hand system that uses MediaPipe for hand tracking, MuJoCo for physics-based simulation, and Arduino for real-time control of robotic movements.

---

## 🧠 Overview
This project uses computer vision to detect hand gestures and map them to robotic finger movements in real time.  
It evolves from basic gesture detection to advanced physics-based simulation using MuJoCo, with future integration into real hardware systems.

---

## ⚙️ Technologies Used
- Python  
- OpenCV  
- MediaPipe (Hand Tracking)  
- NumPy  
- Matplotlib (Early Simulation)  
- MuJoCo (Physics-based Robotic Simulation)  
- Computer Vision  
- Robotics Simulation  

---

## 🚧 Development Progress

### 🔹 Version 1 – Software Simulation
- Implemented hand tracking using MediaPipe  
- Detected finger states (open/close)  
- Simulated servo movement using variables  
- Displayed real-time values on screen  

---

### 🔹 Version 2 – Gesture Arm Simulation
- Added smooth servo motion using interpolation  
- Mapped gestures to robotic arm movement  
- Visualized robotic arm using Matplotlib  
- Improved realism and responsiveness  

---

### 🔷 Version 3 – Advanced Gesture Control (Kinematics)
- Used vector math to calculate real finger joint angles  
- Implemented input filtering for stability  
- Added deadzone and snap threshold to reduce jitter  
- Improved accuracy and responsiveness  
- Displayed FPS and real-time servo angles  

---

### 🔷 Version 4 – Advanced Hand Tracking (MediaPipe Tasks)
- Switched to MediaPipe Tasks API for improved accuracy  
- Extracted continuous finger measurements (distance and angles)  
- Replaced binary detection with precise gesture tracking  
- Enabled smoother and more stable gesture interpretation  
- Built the foundation for physics-based simulation (MuJoCo)  

---

### 🔷 Version 5 – MuJoCo Physics-Based Simulation
- Integrated MediaPipe Tasks for real-time hand tracking  
- Controlled a MuJoCo robotic hand model using gesture input  
- Implemented joint-level control for each finger  
- Added smoothing for stable and realistic motion  
- Achieved real-time physics-based robotic hand simulation  

---

## 🤖 MuJoCo Integration
This project uses **MuJoCo (Multi-Joint dynamics with Contact)** for advanced robotic simulation.

- Simulates a realistic robotic hand using physics-based modeling  
- Uses joint control (`data.ctrl`) to move fingers  
- Maps real-time human hand gestures to robotic joints  
- Enables smooth and natural robotic motion  

This moves the project from simple visualization to real-world robotics simulation.

---

## 🎯 Simulation Preview
This project includes a real-time simulation where:
- Hand gestures are captured using a webcam  
- Finger movements are mapped to robotic joints  
- The robotic hand moves dynamically based on gestures  

---

## 💻 How to Run

1. Install dependencies:
- pip install opencv-python mediapipe numpy matplotlib
2. Run Version 1: python v1_hand_tracking_simulation.py
3. Run Version 2: python v2_gesture_arm_simulation.py
4. Run Version 5 (MuJoCo Simulation): python v5_mujoco_hand_simulation.py

---

## 🔮 Next Steps
- Integrate Arduino for real servo control  
- Improve gesture accuracy  
- Build full robotic hand hardware  

---

## 👨‍💻 Author
Shahel Mohammed
