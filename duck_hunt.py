import cv2
import mediapipe as mp
import numpy as np
import random
import math
import time

# ==============================
# CAMERA SETUP
# ==============================
cap = cv2.VideoCapture(0)
SCREEN_W, SCREEN_H = 960, 720
cap.set(3, SCREEN_W)
cap.set(4, SCREEN_H)

# ==============================
# MEDIAPIPE HANDS
# ==============================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ==============================
# GAME VARIABLES
# ==============================
score = 0
last_shot_time = 0
SHOT_COOLDOWN = 0.5
prev_shoot = False

# ==============================
# LOAD BIRD IMAGE
# ==============================
bird_img = cv2.imread("Bird.png", cv2.IMREAD_UNCHANGED)
bird_img = cv2.resize(bird_img, (80, 80))

# ==============================
# DUCK CLASS
# ==============================
class Duck:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = -80
        self.y = random.randint(80, SCREEN_H // 2)
        self.speed = random.randint(5, 9)
        self.state = "flying"
        self.fall_speed = 0

    def move(self):
        if self.state == "flying":
            self.x += self.speed
            if self.x > SCREEN_W:
                self.reset()
        else:  # falling
            self.fall_speed += 1
            self.y += self.fall_speed
            if self.y > SCREEN_H:
                self.reset()

duck = Duck()

# ==============================
# IMAGE OVERLAY FUNCTION
# ==============================
def overlay_png(bg, png, x, y):
    h, w = png.shape[:2]
    if x < 0 or y < 0 or x + w > bg.shape[1] or y + h > bg.shape[0]:
        return

    if png.shape[2] == 4:
        alpha = png[:, :, 3] / 255.0
        for c in range(3):
            bg[y:y+h, x:x+w, c] = (
                alpha * png[:, :, c] +
                (1 - alpha) * bg[y:y+h, x:x+w, c]
            )
    else:
        bg[y:y+h, x:x+w] = png

# ==============================
# MAIN GAME LOOP
# ==============================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    shoot = False
    finger_x, finger_y = None, None

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        h, w, _ = frame.shape

        index_tip = hand.landmark[8]
        thumb_tip = hand.landmark[4]

        finger_x = int(index_tip.x * w)
        finger_y = int(index_tip.y * h)

        thumb_x = int(thumb_tip.x * w)
        thumb_y = int(thumb_tip.y * h)

        distance = math.hypot(finger_x - thumb_x, finger_y - thumb_y)

        if distance < 65:
            shoot = True
            cv2.putText(frame, "SHOOT", (finger_x + 10, finger_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    # Move duck
    duck.move()

    # Draw bird image
    overlay_png(frame, bird_img, int(duck.x), int(duck.y))

    # Crosshair
    if finger_x and finger_y:
        cv2.circle(frame, (finger_x, finger_y), 10, (0, 0, 255), -1)

        current_time = time.time()
        if shoot and not prev_shoot and current_time - last_shot_time > SHOT_COOLDOWN:
            hit_dist = math.hypot(finger_x - (duck.x + 40), finger_y - (duck.y + 40))
            if hit_dist < 50 and duck.state == "flying":
                score += 1
                duck.state = "falling"
                duck.fall_speed = 2
                last_shot_time = current_time

    prev_shoot = shoot

    # HUD
    cv2.putText(frame, f"Score: {score}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

    cv2.putText(frame, "Pinch fingers to shoot", (20, SCREEN_H - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 2)

    cv2.imshow("Duck Hunt - Hand Gun", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
