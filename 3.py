from tkinter import *
from random import randint as rt
root=Tk()
root.geometry('1200x700')
W, H = 1100, 600
c=Canvas(root,width=W,height=H, bg = 'blue')
c.place(x=50, y=50)
c.create_rectangle(W//3 - 25*2, 0, W//3 + 25*2, H, fill = "grey")
c.create_rectangle(W//3*2 - 25*2, 0, W//3*2 + 25*2, H, fill = "grey")
c.create_rectangle(0, H//3 - 25*2, W, H//3 + 25*2, fill = "grey")
c.create_rectangle(0, H//3*2 - 25*2, W, H//3*2 + 25*2, fill = "grey")

class Main:
    def __init__(self):
        pass
The = Main()

cars = []
class Car:
    def __init__(self):
        self.r = 25
        self.stop = False
        a = rt(0, 1)
        if a:
            self.x = rt(W//3 - self.r, W//3 + self.r) + rt(0,1) * W//3
            self.y = 0
            self.vy = rt(5, 7)
            self.vx = 0
        else:
            self.y = rt(H//3 - self.r, H//3 + self.r) + rt(0,1) * H//3
            self.x = 0
            self.vx = rt(5, 7)
            self.vy = 0
        self.repr = c.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                       fill="black")
        cars.append(self)
    def mytick(self):
        if not (self.stop):
            c.move(self.repr, self.vx, self.vy)
            self.x += self.vx
            self.y += self.vy
            if self.x <= 0:
                self.vx *= -1
            if self.x <= -self.r * 2:
                cars.remove(self)
                Car()
            if self.x >= W + self.r * 2:
                cars.remove(self)
                Car()
            if self.y <= -self.r * 2 or self.y >= H + self.r * 2:
                cars.remove(self)
                Car()
        elif self.stop:
            c.move(self.repr, -self.vx, -self.vy)
            self.x -= self.vx
            self.y -= self.vy
        self.stop = False
for _ in range(5):
    Car()

def key(event):
    if event.keycode == 81:
        root.destroy()

def tick():
    for i in cars:
        i.mytick()
        for j in cars:
            if i.x - j.x <= (i.r + j.r) * 2 and j.x - i.x <= (i.r + j.r) * 2 and i.y - j.y <= (i.r + j.r) * 2 and j.y - i.y <= (i.r + j.r) * 2 and not (i is j):
                first = i
                second = j
                for check in cars:
                    if check == i:
                        first = i
                        second = j
                        break
                    if check == j:
                        first = j
                        second = i
                        break
                first.stop = False
                second.stop = True
    c.after(10, tick)

root.title('BURUNDUK')
root.configure(background='green')
root.bind('<Key>', key)
tick()
root.mainloop()