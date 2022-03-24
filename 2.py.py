from tkinter import *
from random import randint as rt
from math import *

root = Tk()
W, H = 1920, 1080
cnv = Canvas(root, width=W, height=H)
cnv.pack()


class Main:
    def __init__(self):
        self.pause = False

The = Main()

def key(event):
    if event.keycode == 32:
        if The.pause:
            The.pause = False
        else:
            The.pause = True
    else:
        root.destroy()


rectangles = []


class Rectangle:
    def __init__(self):
        r = rt(5, 200)
        self.x1, self.y1, self.z1 = -r, -r, r
        self.x2, self.y2, self.z2 = -r, r, r
        self.x3, self.y3, self.z3 = r, r, r
        self.x4, self.y4, self.z4 = r, -r, r

        self.x5, self.y5, self.z5 = -r, -r, -r
        self.x6, self.y6, self.z6 = -r, r, -r
        self.x7, self.y7, self.z7 = r, r, -r
        self.x8, self.y8, self.z8 = r, -r, -r

        self.spawnx = rt(0, W)
        self.spawny = rt(0, H)

        self.a = radians(rt(4, 10))

        rectangles.append(self)


for _ in range(45):
    Rectangle()


def animate():

    if not The.pause:

        cnv.delete("all")

        for i in rectangles:

            i.x1, i.y1 = povorot(i.x1, i.y1, i.a)
            i.x1, i.z1 = povorot(i.x1, i.z1, i.a)
            i.y1, i.z1 = povorot(i.y1, i.z1, i.a)

            i.x2, i.y2 = povorot(i.x2, i.y2, i.a)
            i.x2, i.z2 = povorot(i.x2, i.z2, i.a)
            i.y2, i.z2 = povorot(i.y2, i.z2, i.a)

            i.x3, i.y3 = povorot(i.x3, i.y3, i.a)
            i.x3, i.z3 = povorot(i.x3, i.z3, i.a)
            i.y3, i.z3 = povorot(i.y3, i.z3, i.a)

            i.x4, i.y4 = povorot(i.x4, i.y4, i.a)
            i.x4, i.z4 = povorot(i.x4, i.z4, i.a)
            i.y4, i.z4 = povorot(i.y4, i.z4, i.a)

            i.x5, i.y5 = povorot(i.x5, i.y5, i.a)
            i.x5, i.z5 = povorot(i.x5, i.z5, i.a)
            i.y5, i.z5 = povorot(i.y5, i.z5, i.a)

            i.x6, i.y6 = povorot(i.x6, i.y6, i.a)
            i.x6, i.z6 = povorot(i.x6, i.z6, i.a)
            i.y6, i.z6 = povorot(i.y6, i.z6, i.a)

            i.x7, i.y7 = povorot(i.x7, i.y7, i.a)
            i.x7, i.z7 = povorot(i.x7, i.z7, i.a)
            i.y7, i.z7 = povorot(i.y7, i.z7, i.a)

            i.x8, i.y8 = povorot(i.x8, i.y8, i.a)
            i.x8, i.z8 = povorot(i.x8, i.z8, i.a)
            i.y8, i.z8 = povorot(i.y8, i.z8, i.a)

            colors = {
                1:"red",
                2:"blue",
                3:"green",
                4:"orange"
                }
            color = colors[rt(1,4)]
            cnv.create_polygon(i.spawnx + i.x1, i.spawny + i.y1, i.spawnx + i.x2, i.spawny + i.y2,
                               i.spawnx + i.x3, i.spawny + i.y3,i.spawnx + i.x4, i.spawny + i.y4,
                               i.spawnx + i.x1, i.spawny + i.y1, fill=color)

            cnv.create_polygon(i.spawnx + i.x5, i.spawny + i.y5, i.spawnx + i.x6, i.spawny + i.y6,
                               i.spawnx + i.x7, i.spawny + i.y7,i.spawnx + i.x8, i.spawny + i.y8,
                               i.spawnx + i.x5, i.spawny + i.y5, fill=color)

            cnv.create_polygon(i.spawnx + i.x1, i.spawny + i.y1, i.spawnx + i.x2, i.spawny + i.y2,
                               i.spawnx + i.x6, i.spawny + i.y6, i.spawnx + i.x5, i.spawny + i.y5,
                               i.spawnx + i.x1, i.spawny + i.y1, fill=color)

            cnv.create_polygon(i.spawnx + i.x3, i.spawny + i.y3, i.spawnx + i.x4, i.spawny + i.y4,
                               i.spawnx + i.x8, i.spawny + i.y8, i.spawnx + i.x7, i.spawny + i.y7,
                               i.spawnx + i.x3, i.spawny + i.y3, fill=color)

            cnv.create_polygon(i.spawnx + i.x2, i.spawny + i.y2, i.spawnx + i.x3, i.spawny + i.y3,
                               i.spawnx + i.x7, i.spawny + i.y7, i.spawnx + i.x6, i.spawny + i.y6,
                               i.spawnx + i.x2, i.spawny + i.y2, fill=color)

            cnv.create_line(i.spawnx + i.x1, i.spawny + i.y1, i.spawnx + i.x2, i.spawny + i.y2)
            cnv.create_line(i.spawnx + i.x2, i.spawny + i.y2, i.spawnx + i.x3, i.spawny + i.y3)
            cnv.create_line(i.spawnx + i.x3, i.spawny + i.y3, i.spawnx + i.x4, i.spawny + i.y4)
            cnv.create_line(i.spawnx + i.x4, i.spawny + i.y4, i.spawnx + i.x1, i.spawny + i.y1)

            cnv.create_line(i.spawnx + i.x5, i.spawny + i.y5, i.spawnx + i.x6, i.spawny + i.y6)
            cnv.create_line(i.spawnx + i.x6, i.spawny + i.y6, i.spawnx + i.x7, i.spawny + i.y7)
            cnv.create_line(i.spawnx + i.x7, i.spawny + i.y7, i.spawnx + i.x8, i.spawny + i.y8)
            cnv.create_line(i.spawnx + i.x8, i.spawny + i.y8, i.spawnx + i.x5, i.spawny + i.y5)

            cnv.create_line(i.spawnx + i.x1, i.spawny + i.y1, i.spawnx + i.x5, i.spawny + i.y5)
            cnv.create_line(i.spawnx + i.x2, i.spawny + i.y2, i.spawnx + i.x6, i.spawny + i.y6)
            cnv.create_line(i.spawnx + i.x3, i.spawny + i.y3, i.spawnx + i.x7, i.spawny + i.y7)
            cnv.create_line(i.spawnx + i.x4, i.spawny + i.y4, i.spawnx + i.x8, i.spawny + i.y8)

    cnv.after(50, animate)

def povorot(x, y, a):
     return x * cos(a) - y * sin(a), x * sin(a) + y * cos(a)

animate()
root.bind('<Key>', key)

mainloop()
