# Gesture Controlled Robotic Hand

A gesture-controlled robotic hand system that uses MediaPipe for hand tracking, MuJoCo for physics-based simulation, and Arduino for real-time control of robotic movements.

---
🎥 robotic hand demo


![mujoco_1080x608](https://github.com/user-attachments/assets/32693cd3-f3da-4d8d-984d-56c164360f61)

![handmovements_1080x608](https://github.com/user-attachments/assets/b643875a-8f97-447e-89ec-f45bcd9de111)



## 🧠 Overview
This project enables natural human-computer interaction by capturing hand gestures using a webcam and translating them into robotic finger movements.

It integrates:
	•	MediaPipe for hand tracking
	•	MuJoCo for physics-based simulation
	•	Arduino for real-world hardware control

The system evolves from basic gesture detection to a fully simulated robotic hand, with ongoing integration into a physical robotic hand prototype.

---

🎯 Problem Statement

Traditional robotic systems rely on manual controllers or pre-programmed instructions.
This project aims to develop an intuitive, real-time gesture-based control system that allows users to control robotic hands naturally using human gestures.

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

## 🔬 Key Features

- 🎯 **Real-time hand gesture tracking**  
- 🤖 **Joint-level robotic finger control**  
- 📐 **Accurate angle calculation using kinematics**  
- 🎮 **Smooth motion using interpolation**  
- 🧊 **Noise reduction (dead zones + filtering)**  
- ⚡ **Real-time FPS and performance monitoring**  
- 🧩 **Modular design (Simulation + Hardware)**  

  ---


 ## 🌍 Applications

This gesture-controlled robotic hand system has potential applications in various real-world domains:

- 🦾 **Prosthetics & Assistive Technology**  
  Can be used to develop advanced prosthetic hands controlled by natural human gestures.

- 🏥 **Medical & Rehabilitation**  
  Useful in physiotherapy and rehabilitation systems for hand movement training and recovery.

- 🏭 **Industrial Robotics**  
  Enables intuitive control of robotic arms for tasks in manufacturing and automation.

- 🎮 **Virtual Reality (VR) & Gaming**  
  Enhances user interaction by enabling gesture-based control in immersive environments.

- 🧠 **Human-Computer Interaction (HCI)**  
  Provides a natural and contactless interface for controlling machines and digital systems.

- 🎓 **Education & Research**  
  Serves as a practical platform for learning robotics, AI, and embedded systems.

- 🪖 **Defense & Hazardous Environments**  
  Can be used for remote operation of robotic systems in dangerous or inaccessible areas.


----

⚙️ How It Works

<img width="178" height="309" alt="Screenshot 2026-04-27 at 9 31 43 PM" src="https://github.com/user-attachments/assets/293030ca-f1d0-46ad-9bad-fc01105e823a" />



1. Capture Input
    A webcam continuously captures real-time video of hand movements.
2. Hand Landmark Detection
    MediaPipe processes each frame to detect hand landmarks and track finger positions.
3. Gesture Analysis
    Finger joint angles are calculated using vector-based computations.
4. Mapping to Actuation
    The calculated angles are mapped to corresponding servo motor positions.
5. Data Transmission
    The processed data is transmitted to the Arduino via serial communication (PySerial).
6. Hardware Execution
    The Arduino interprets the received data and controls the servo motors accordingly.
7. Robotic Movement
    The robotic hand replicates human finger movements in real time.

----   
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

🔷 Version 6 – Hardware Integration (Arduino + Servos)

* Established serial communication between Python and Arduino using PySerial
* Transmitted real-time finger angle data from computer vision system to hardware
* Controlled multiple servo motors to replicate finger movements
* Implemented angle mapping and calibration for each finger
* Integrated external power supply with buck converter for stable servo operation
* Achieved real-time gesture-based control of the physical robotic hand
  
---  

🔷 Version 7 – System Optimization & Stability Improvements

* Improved motion smoothness using advanced filtering techniques
* Reduced servo jitter through deadzone tuning and signal stabilization
* Optimized serial communication for faster and reliable data transfer
* Fine-tuned finger angle mapping for better accuracy and realism
* Enhanced overall system performance and responsiveness
* Conducted extensive testing for consistent real-time operation

---


🤖 Physical Robotic Hand

The robotic hand is implemented using Arduino and servo motors.

<img width="471" height="522" alt="Screenshot 2026-04-08 at 7 44 34 AM" src="https://github.com/user-attachments/assets/6330d6e1-1118-4a4a-a4ec-e96972c22eac" />

🔌 Components

	•	Arduino Nano
	•	Servo Motors
	•	External Power Supply
	•	Jumper Wires
	•	Robotic Hand Structure

⚙️ Working

	•	Arduino controls servos to move fingers
	•	Fingers successfully perform open and close motion
	•	Mechanical system (strings/joints) converts rotation into finger movement
  
---

🤖 MuJoCo Integration
This project uses **MuJoCo (Multi-Joint dynamics with Contact)** for advanced robotic simulation.

- Simulates a realistic robotic hand using physics-based modeling  
- Uses joint control (`data.ctrl`) to move fingers  
- Maps real-time human hand gestures to robotic joints  
- Enables smooth and natural robotic motion  

This moves the project from simple visualization to real-world robotics simulation.

---

 🎯 Simulation Preview
<img width="3840" height="2160" alt="shadow_hand" src="https://github.com/user-attachments/assets/d8606925-f19a-44af-8293-93ce216bfd9d" />

This project includes a real-time simulation where:
- Hand gestures are captured using a webcam  
- Finger movements are mapped to robotic joints  
- The robotic hand moves dynamically based on gestures  
---
📘 Detailed Setup Guide (Step-by-Step)

Follow this guide to set up and run the Gesture-Controlled Robotic Hand project from scratch.

🚀 Quick Start (Recommended – Fastest Way)

👉 If you just want to run the project quickly, follow these steps:
🔹 Step 1: Clone the Repository
 
 • git clone https://github.com/your-username/gesture-robotic-hand.git
 • cd gesture-robotic-hand
 
🔹 Step 2: Run Setup Script
▶️ Mac / Linux

run chmod +x setup.sh
./setup.sh

▶️ Windows

run setup.bat

🔹 Step 3: Run the Project

👉 Choose one:

🧪 Simulation Mode

  source sim_env/bin/activate
  python v5_mujoco_hand_simulation.py

🤖 Hardware Mode

source hardware_env/bin/activate
python v7_hardware_integration.py
---
🛠️ Manual Setup (Detailed)

(Use this if the quick setup doesn’t work or you want full control)
🔹 Step 1: Clone the Repository
    git clone https://github.com/your-username/gesture-robotic-hand.git
    cd gesture-robotic-hand
🔹 Step 2: Create Virtual Environments

🧠 Simulation Environment

  python -m venv sim_env
  source sim_env/bin/activate   # Mac/Linux

🤖 Hardware Environment

   python -m venv hardware_env
   source hardware_env/bin/activate
   
🔹 Step 3: Install Dependencies

 For Simulation  
 pip install opencv-python mediapipe numpy matplotlib mujoco

 For Hardware
 pip install opencv-python mediapipe numpy pyserial
 
 🔹 Step 4: Run the Project
 
  🧪 Simulation
  
  source sim_env/bin/activate
  python v5_mujoco_hand_simulation.py
  
  🤖 Hardware

  source hardware_env/bin/activate
  python v7_hardware_integration.py
  
---
🤖 Hardware Setup (Detailed)

🔌 Components Required

	•	Arduino Nano
	•	Servo Motors (SG90 / MG996R)
	•	External Power Supply(5V–6V recommended)
	•	Jumper Wires
	•	Breadboard (optional but recommended)
	•	Buck Converter (DC-DC Step Down Module)
⸻

⚙️ Servo Wiring (Important)

Each servo has 3 wires:

	•	🟤 Brown / Black → GND
	•	🔴 Red → VCC (5V)
	•	🟠 Orange / Yellow → Signal (Control Pin)
	
⸻  

⚙️ What is a Buck Converter?

A buck converter steps down higher voltage (e.g., 9V/12V) to a stable 5V required by servos.

👉 This prevents:

	•	Arduino resets
	•	Servo jitter
	•	Overheating
	
 ⸻   
 
 🔌 Complete Wiring (WITH Buck Converter)

 <img width="483" height="312" alt="Screenshot 2026-04-27 at 9 22 24 PM" src="https://github.com/user-attachments/assets/8f7a8ca2-7fb7-47cf-91f5-f3b8ead18963" />


🔹 Step 1: Power Input to Buck Converter

	•	Connect battery/adaptor:
	•	+ (Positive) → IN+ (Buck Converter)
	•	– (Negative) → IN– (Buck Converter)

⸻

🔹 Step 2: Set Output Voltage ⚠️

	•	Adjust potentiometer on buck converter
	•	Use multimeter
	•	Set output to 5V

⸻

🔹 Step 3: Power Servos

	•	Buck Converter OUT+ → All servo Red wires
	•	Buck Converter OUT– → All servo Brown wires

⸻

🔹 Step 4: Connect Arduino

	•	Arduino GND → Buck Converter OUT– (COMMON GROUND)

👉 This step is mandatory

⸻

🔹 Step 5: Signal Connections

	•	Thumb → D3
	•	Index → D5
	•	Middle → D6
	•	Ring → D9
	•	Pinky → D10
  
⸻
⚙️ Step-by-Step Execution

	1.	Connect power source → buck converter input
	2.	Adjust output voltage to 5V
	3.	Connect servos to buck converter output
	4.	Connect Arduino GND to buck converter GND
	5.	Connect servo signals to Arduino pins
	6.	Upload Arduino code
	7.	Test finger movement

⸻

⚠️ Common Mistakes

❌ Not setting buck converter to 5V

👉 Can damage servos

❌ No common ground

👉 Servos won’t respond

❌ Loose connections

👉 Jitter / random movement

❌ Weak power supply

👉 Servos stop or reset

___

⚠️ Common Issues & Solutions

❌ Issue: ModuleNotFoundError

Cause: Required Python packages are not installed

Solution:
pip install opencv-python mediapipe numpy matplotlib mujoco
---

❌ Issue: Camera Not Opening

Cause: Webcam not accessible or already in use

Solution:
	•	Check camera permissions
	•	Close other apps using the camera
	•	Try changing camera index:
   cv2.VideoCapture(0)
---
❌ Issue: Hand Not Detected Properly

Cause: Poor lighting or unclear hand position

Solution:
	•	Use good lighting
	•	Keep hand fully visible
	•	Avoid cluttered background

⸻

❌ Issue: MuJoCo Not Running

Cause: Missing dependencies or OpenGL issue
Solution:
pip install mujoco glfw
Mac users:
brew install glfw

⸻

❌ Issue: Low FPS / Lag

Cause: High processing load

Solution:
	•	Reduce camera resolution
	•	Close background apps
	•	Optimize loops in code

⸻

❌ Issue: Servo Not Moving

Cause: Wiring or power issue

Solution:
	•	Check signal pin connections
	•	Use external power supply (NOT Arduino 5V)
	•	Verify Arduino code is uploaded

⸻

❌ Issue: Servo Jitter / Noise

Cause: Unstable power or tight mechanical setup

Solution:
	•	Use stable 5V power (buck converter recommended)
	•	Loosen strings/mechanical tension
	•	Add smoothing in code

⸻

❌ Issue: Wrong Finger Movement

Cause: Incorrect servo mapping

Solution:
	•	Check pin mapping
	•	Adjust angle values in code
	•	Reverse servo direction if needed

⸻

❌ Issue: Arduino Not Detected

Cause: Wrong port or driver issue

Solution:
	•	Select correct COM port in Arduino IDE
	•	Install CH340 driver (if needed)
	•	Reconnect USB cable

⸻

❌ Issue: Serial Communication Not Working

Cause: Port mismatch or baud rate mismatch

Solution:
	•	Match baud rate in both Python and Arduino
	•	Example:serial.Serial('COM3', 9600)
	
❌ Issue: Servos Resetting / Arduino Restarting

Cause: Insufficient power supply

Solution:
	•	Use external power (≥2A recommended)
	•	Do NOT power servos from Arduino

⸻

❌ Issue: Buck Converter Not Working

Cause: Incorrect voltage setting

Solution:
	•	Use multimeter
	•	Adjust output to 5V before connecting servos

⸻
## 💡 Key Learnings

- Real-time hand tracking using MediaPipe  
- Gesture-to-motion mapping using kinematics  
- Serial communication between Python and Arduino  
- Servo motor control and calibration  
- Integration of simulation and physical hardware

---

## 🚀 Current Status

The following features have been successfully implemented:

- 🔌 **Real-Time Hardware Integration**  
  Achieved direct communication between gesture input and Arduino for live servo control.

- 🖐️ **Independent Finger Control**  
  Implemented precise control of each finger using real-time gesture angle mapping.

- 🎯 **Improved Gesture Accuracy**  
  Enhanced tracking stability using filtering, smoothing, and noise reduction techniques.

- 🤖 **Complete Physical Robotic Hand**  
  Developed a functional robotic hand with optimized mechanical design and movement.

---

## 🔮 Future Enhancements

- 📡 **Wireless Communication**  
  Implement Bluetooth/WiFi modules for untethered control of the robotic hand.

- 🧤 **Glove-Based Control System** *(Optional Upgrade)*  
  Integrate flex sensors with a wearable glove for more precise gesture input.

- ⚡ **Performance Optimization**  
  Improve system efficiency and reduce latency for faster real-time response.

⸻

## 👨‍💻 Author

**Shahel Mohammed**  
BCA – AI, ML & Robotics  
Yenepoya University  
