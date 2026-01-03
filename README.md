# 🦆 Duck Hunt Hand Gesture Game 🎯

A modern recreation of the classic **Duck Hunt game** using **hand gesture recognition**.
Players aim and shoot flying birds using their **index finger** detected via a webcam — no mouse or keyboard required!

This project combines **Computer Vision**, **AI**, and **Game Development** using Python.

## Features
- 🖐️ Real-time Hand Tracking using MediaPipe
- 🎯 Finger-based Shooting Mechanism
- 🐦 Animated Bird Movement
- ⬇️ Bird Falling Animation when Shot
- 📊 Live Score Tracking
- 📷 Webcam-Based Gameplay
- ⚡ Single-file Python implementation
- 🎮 Inspired by the classic Duck Hunt game


## 🛠️ Technologies Used
- Python 3.10
- OpenCV
- MediaPipe
- NumPy

## Project Structure

    ```bash
    duck-hunt-hand-gesture/
    │
    ├── duck_hunt.py        # Main game file
    ├── Bird.png            # Bird sprite image
    ├── requirements.txt    # Python dependencies
    ├── .gitignore          # Ignored files & folders
    └── README.md           # Project documentation


## Installation & Setup
## 1.Clone the Repository

    '''bash
    git clone https://github.com/Vaishuu-creator/duck-hunt-hand-gesture.git
    cd duck-hunt-hand-gesture

## 2.Create Virtual Environment (Recommended)

    '''bash
    python -m venv venv
    source venv/Scripts/activate   # Windows (Git Bash)

## 3.Install Dependencies
    '''bash
    pip install -r requirements.txt

## ▶️ How to Run the Game
    '''bash
    python duck_hunt.py

✔ Ensure your webcam is connected
✔ Allow camera permission when prompted

## 🎯 How to Play
- Open palm to enable hand tracking
- Point your index finger to aim
- Keep the finger tip over the bird
- Perform a shoot gesture (finger steady)

Hit bird → bird falls → score increases 🎉
