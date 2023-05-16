from tkinter import *

root = Tk()
root.title('Canvas')
canvas = Canvas(root, width=400, height=400, bg='yellow')
x0 = 199
y0 = 199
y1 = 201
x1 = 201
for i in range(18):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5

canvas.pack()
root.mainloop()
