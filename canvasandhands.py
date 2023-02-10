import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Function to receive output from MediaPipe and display on canvas
def display_mediapipe_output(canvas, visualizer_options, visualization_stream):
    while True:
        packets = visualization_stream.Next()
        if not packets:
            break
        for packet in packets:
            if packet.index == 1:
                image = packet.GetValue()
                color_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                height, width, _ = color_image.shape
                image = np.array(color_image)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)
                canvas.create_image(0, 0, image=image, anchor=tk.NW)
                canvas.pack()

# Function to display multiple windows on canvas
def display_multiple_windows():
    root = tk.Tk()
    root.title("MediaPipe Output")
    canvas_width = 720
    canvas_height = 720

    # Create 3 canvas for different outputs
    canvas1 = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas1.pack(side="left")
    canvas2 = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas2.pack(side="left")
    canvas3 = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas3.pack(side="left")

    # Call display_mediapipe_output function to receive output from MediaPipe
    display_mediapipe_output(canvas1, None, visualization_stream)
    display_mediapipe_output(canvas2, None, visualization_stream)
    display_mediapipe_output(canvas3, None, visualization_stream)
    root.mainloop()

if __name__ == '__main__':
    display_multiple_windows()