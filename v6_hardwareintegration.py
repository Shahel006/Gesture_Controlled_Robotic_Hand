import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import time
import serial

# -----------------------------
# SERIAL SETUP (MAC)
# -----------------------------
ser = serial.Serial('/dev/cu.usbserial-110', 9600, timeout=1)
time.sleep(2)

# -----------------------------
# MediaPipe Setup
# -----------------------------
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

# -----------------------------
# Camera
# -----------------------------
cap = cv2.VideoCapture(0)

# -----------------------------
# SMOOTHING VARIABLES
# -----------------------------
prev_vals = np.array([30, 30, 30, 30, 30], dtype=float)

# -----------------------------
# Finger angle function
# -----------------------------
def finger_angle(a, b, c):
    a = np.array([a.x, a.y])
    b = np.array([b.x, b.y])
    c = np.array([c.x, c.y])

    ba = a - b
    bc = c - b

    cos_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(np.clip(cos_angle, -1, 1))

# -----------------------------
# Bend mapping
# -----------------------------
def get_bend(angle):
    bend = np.interp(angle, [0.2, 1.7], [0, 2.0])
    return np.clip(2.0 - bend, 0, 2.0)

# -----------------------------
# Range mapping
# -----------------------------
def map_range(val, out_min, out_max):
    return int(np.clip(
        np.interp(val, [0, 2.0], [out_min, out_max]),
        out_min,
        out_max
    ))

# -----------------------------
# MAIN LOOP
# -----------------------------
while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    # Default = open hand
    values = np.array([30, 30, 30, 30, 30], dtype=float)

    if result.hand_landmarks:

        hand = result.hand_landmarks[0]

        # -----------------------------
        # 🔥 THUMB (FINAL FIX - PALM METHOD)
        # -----------------------------
        thumb_tip = hand[4]
        palm = hand[0]

        thumb_dist = np.linalg.norm([
            thumb_tip.x - palm.x,
            thumb_tip.y - palm.y
        ])

        # tuned range
        thumb_bend = np.interp(thumb_dist, [0.15, 0.45], [0, 2.0])
        thumb_bend = np.clip(thumb_bend, 0, 2.0)

        # -----------------------------
        # OTHER FINGERS
        # -----------------------------
        index_bend  = get_bend(finger_angle(hand[5], hand[6], hand[8]))
        middle_bend = get_bend(finger_angle(hand[9], hand[10], hand[12]))
        ring_bend   = get_bend(finger_angle(hand[13], hand[14], hand[16]))
        pinky_bend  = get_bend(finger_angle(hand[17], hand[18], hand[20]))

        # -----------------------------
        # FINAL CALIBRATION
        # -----------------------------
        values[0] = map_range(thumb_bend * 1.4, 30, 180)   # thumb strong + natural
        values[1] = map_range(index_bend, 30, 180)
        values[2] = map_range(middle_bend, 30, 180)
        values[3] = map_range(ring_bend, 30, 180)
        values[4] = map_range(pinky_bend * 3.0, 20, 180)   # strong but controlled

    # -----------------------------
    # SMOOTHING
    # -----------------------------
    values = 0.7 * prev_vals + 0.3 * values
    prev_vals = values

    # Convert to int
    t, i, m, r, p = values.astype(int)

    # Debug print
    print(f"T:{t} I:{i} M:{m} R:{r} P:{p}")

    # -----------------------------
    # SEND TO ARDUINO
    # -----------------------------
    data_string = f"{t},{i},{m},{r},{p}\n"

    try:
        ser.write(data_string.encode())
    except:
        print("⚠️ Serial error")

    # -----------------------------
    # DISPLAY CAMERA
    # -----------------------------
    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.01)

cap.release()
ser.close()
cv2.destroyAllWindows()