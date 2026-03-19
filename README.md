# Gesture_Controlled_Robotic_Hand

# Gesture Controlled Robotic Hand

A gesture-controlled robotic hand system using MediaPipe and Arduino that replicates human hand movements in real time.

---

## 🧠 Overview
This project uses computer vision to detect hand gestures and map them to robotic finger movements.  
Currently, the system simulates servo movement and will be extended to real hardware control.

---

## ⚙️ Technologies Used
- Python (OpenCV, MediaPipe)
- Arduino (for future integration)
- Computer Vision

---

## 🚧 Development Progress

### 🔹 Version 1 – Software Simulation
- Implemented hand tracking using MediaPipe  
- Detected finger states (open/close)  
- Simulated servo movement using variables  
- Displayed real-time values on screen
  
### 🔹 Version 2 – Gesture Arm Simulation
- Added smooth servo motion using interpolation  
- Mapped gestures to robotic arm movement  
- Visualized robotic arm using matplotlib  
- Improved realism and responsiveness  

---

## 💻 How to Run

1. Install dependencies:
pip install opencv-python mediapipe numpy matplotlib

2. Run Version 1:
python v1_hand_tracking_simulation.py

3. Run Version 2:
python v2_gesture_arm_simulation.py

---

## 🔮 Next Steps
- Integrate Arduino for real servo control  
- Improve gesture accuracy  
- Build full robotic hand hardware  

---

## 👨‍💻 Author
Shahel Mohammed
