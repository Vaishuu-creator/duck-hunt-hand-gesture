# Duck Hunt – Hand Gesture Controlled Game

A fun **gesture-controlled game** where you shoot flying ducks using **hand gestures** detected from your webcam — no keyboard or mouse needed!  
This project uses **OpenCV**, **MediaPipe Hands**, and **Python** to create an interactive computer vision game.

---

## What is this project about?

This project turns your webcam into a **gesture-based game controller**.  
You aim using your **index finger**, and a **pinch gesture** (thumb + index finger) acts like a trigger to shoot flying ducks.

Key features:
- Real-time hand landmark detection
- Gesture-based shooting using pinch distance
- Duck movement, collision detection & falling animation
- Score tracking and cooldown system
- PNG image overlay with transparency

---

## How it Works

1. Webcam captures live video feed.
2. MediaPipe Hands detects hand landmarks.
3. Index finger tip position becomes the **aiming crosshair**.
4. Pinch gesture (thumb + index) triggers a **shoot action**.
5. If a duck is in range when you shoot → score increase and duck falls.
6. Ducks reset and fly again continuously.

---

## Technologies Used

- Python
- OpenCV
- MediaPipe Hands
- NumPy
- Math & Time modules

---

## File Structure

duck-hunt-hand-gesture/  
│  
├── main.py - Main game script  
├── Bird.png - Duck / bird sprite with transparency  
├── requirements.txt - Python dependencies  
└── README.md - Project documentation  

---

## Setup Instructions

### 1. Clone the Repository

    git clone https://github.com/Vaishuu-creator/duck-hunt-hand-gesture
    cd duck-hunt-hand-gesture

### 2. Install Dependencies

Install requirements using:

    pip install -r requirements.txt

(Make sure Python 3.8+ is installed)

---

## How to Play

1. **Run the game**
   ```bash
   python main.py
2. Move your **index finger** to aim.
3. **Pinch** (thumb + index close together) to shoot.
4. Score increases when you hit a flying duck.
5. Press **ESC** to quit.

---

## Controls

Action | Gesture 
 ------------ | ------------- 
Aim | Move index finger  
Shoot | Pinch gesture
Exit Game | Press ESC 

---

## Notes

- Make sure your webcam is connected and functioning properly.
- Play in a well-lit environment for best hand detection accuracy.
- PNG image needs to remain in the same folder as main.py.

---

## Future Enhancements

- Add multiple ducks
- Add sounds (gunshots, hits)
- Add levels & difficulty modes
- Two-hand gestures
- Mobile / AR version

---

## License

This project is licensed under the MIT License — see the LICENSE file for details.

---

## Author

### Vaishali Murugesan
Final Year Computer Technology Student  
Aspiring AI / Software Engineer  
  
If you find this project cool, give it a star!
