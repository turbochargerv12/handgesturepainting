import tkinter as tk

root = tk.Tk()
root.title("Python Paint Brush")

canvas = tk.Canvas(root, height=400, width=400, background="white")
canvas.pack()

# initialize color to black
color = "black"

def change_color(new_color):
    global color
    color = new_color

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_line(x1, y1, x2, y2, fill=color, width=5, capstyle=tk.ROUND, smooth=True)

canvas.bind("<B1-Motion>", paint)

# create a menu
menu = tk.Menu(root)
root.config(menu=menu)

color_menu = tk.Menu(menu)
menu.add_cascade(label="Colors", menu=color_menu)

color_menu.add_command(label="Red", command=lambda: change_color("red"))
color_menu.add_command(label="Green", command=lambda: change_color("green"))
color_menu.add_command(label="Blue", command=lambda: change_color("blue"))

root.mainloop()
