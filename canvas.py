import tkinter as tk

root = tk.Tk()
root.title("Python Paint Brush")

canvas = tk.Canvas(root, height=400, width=400, background="white")
canvas.pack()

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_line(x1, y1, x2, y2, fill="black", width=5, capstyle=tk.ROUND, smooth=True)

canvas.bind("<B1-Motion>", paint)

root.mainloop()
