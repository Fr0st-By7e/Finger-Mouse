# AI Hand Gesture Mouse Control

This project uses computer vision and hand gesture recognition that allows users to control the mouse cursor and perform actions like moving, clicking, and scrolling based on hand and finger movements.

## Features
- **Real-time Hand Gesture Detection**: Uses machine learning to detect hand gestures through a webcam.
- **Multi-functionality**: Allows moving the cursor, clicking, and scrolling.
- **User-Friendly**: Easy setup and use without requiring any complex configurations and intuitive controls.
  
## Requirements
- Python 3.x (that supports MediaPipe)
- A camera/webcam

## Repository Contents
- **hand_tracker_module.py**: Module that detects hand and finger positions
- **virtual_mouse.py**: Virtual mouse

## Installation

Follow these steps to get the project up and running on your local machine.

### 1. Clone the repository:
```bash
git clone https://github.com/Fr0st-By7e/Finger-Mouse.git
```

### 2. Navigate to the project directory:
```bash
cd AI-FINGER-MOUSE
```

### 3. Install the required dependencies:
```bash
pip install opencv-python
pip install mediapipe
pip install autopy
pip install pynput
pip install numpy
```

## Usage

1. Connect webcam to your system
2. Run the 'virtual_mouse.py' file
3. Control the mouse in different modes using your hands
4. Press 'q' to quit

## Gestures and Actions

### Moving mode:
Raise your index finger only.

### Clicking mode:
Raise both your index and middle fingers only and touch the finger tips to click.

### Scrolling mode:
Point your thumb out
- To scroll-up: Raise your pinky finger while the thumb is out.
- To scroll-down: Raise both your pinky and ring fingers while the thumb is out.

## How it Works

- The program uses MediaPipe to track the user's hand gestures in real-time using a webcam.
- OpenCV is used for capturing and processing the webcam feed.
- Numpy is used to convert the co-ordinates for easy tracking
- Autopy is used to move and click the mouse
- Pynput is used to scroll

## Troubleshooting

- Poor Performance: If the FPS is low or gestures are not recognized correctly, try adjusting the camera resolution or the frameR and smoothening variables (Line 8-14 in virtual_mouse.py).
- Scroll Sensitivity: If the scrolling speed is too fast or slow, decrease or increase the scroll range accordingly (Line 79-82 in virtual_mouse.py).

## License

This project is open-source and released under the MIT License.