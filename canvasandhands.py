import cv2
import tkinter as tk

# Load the hand cascade classifier
hand_cascade = cv2.CascadeClassifier('hand.xml')

# Start the OpenCV video capture
cap = cv2.VideoCapture(0)

# Create the Tkinter window and canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack()

# Function to update the canvas pointer position
def update_pointer_position(x, y):
    canvas.coords(pointer, x, y, x + 10, y + 10)

# Create the canvas pointer
pointer = canvas.create_oval(0, 0, 10, 10, fill='red')

# Function to process video frames
def process_frame():
    # Read a video frame from the OpenCV capture
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands in the frame
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    # If a hand is detected
    if len(hands) > 0:
        # Get the hand bounding box
        (x, y, w, h) = hands[0]

        # Update the canvas pointer position
        update_pointer_position(x + w // 2, y + h // 2)

    # Schedule the next frame processing
    root.after(30, process_frame)

# Start the frame processing
process_frame()

# Start the Tkinter main loop
root.mainloop()