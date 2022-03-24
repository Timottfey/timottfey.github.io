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
            self.x = rt(W//3 - self.r, W//3 + self.r) + rt(0, 1) * W//3
            self.y = rt(self.r, self.r*2)
            self.vy = rt(5, 7)
            self.vx = 0
        else:
            self.y = rt(H//3 - self.r, H//3 + self.r) + rt(0, 1) * H//3
            self.x = rt(self.r, self.r*2)
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
            if self.x <= -self.r * 2 or self.y <= -self.r * 2 or self.y >= H + self.r * 2 or self.x >= W + self.r * 2:
                cars.remove(self)
                Car()
        elif self.stop and perekrestok(self.x, self.y, self.r):
            c.move(self.repr, -self.vx, -self.vy)
            self.x -= self.vx
            self.y -= self.vy
        self.stop = False
for _ in range(2):
    Car()

mans = []
class Man:
    def __init__(self):
        self.x, self.y, self.r = rt(50, W-50), rt(50, H-50), 10
        self.vx, self.vy = rt(2, 3), rt(2, 3)
        self.repr = self.repr = c.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r,
                                                   self.y + self.r, fill="white")
        mans.append(self)
    def mytick(self):
        c.move(self.repr, self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        if self.x <= -self.r * 2 or self.y <= -self.r * 2 or self.y >= H + self.r * 2 or self.x >= W + self.r * 2:
            mans.remove(self)
            Man()
for _ in range(5):
    Man()

def perekrestok(x, y, r):
    if (x-r < W//3 + 25*2 and y+r > W//3 - 25*2) or (x-r < (W//3)*2 + 25*2 and y+r > (W//3)*2 - 25*2):
        return False
    return True

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
            if i.x - j.x <= (i.r + j.r) and j.x - i.x <= (i.r + j.r) and i.y - j.y <= (
                    i.r + j.r) and j.y - i.y <= (i.r + j.r) and not (i is j):
                c.move(i.repr, 1000, 1000)
                i.x += 1000
                i.y += 1000
                c.move(j.repr, 1000, 1000)
                j.x += 1000
                j.y += 1000
                cars.remove(i)
                cars.remove(j)
                Car()
                Car()
        for j in mans:
            if i.x - j.x <= (i.r + j.r) * 2 and j.x - i.x <= (i.r + j.r) * 2 and i.y - j.y <= (
                    i.r + j.r) * 2 and j.y - i.y <= (i.r + j.r) * 2 and not (i is j):
                i.stop = True
            if i.x - j.x <= (i.r + j.r) and j.x - i.x <= (i.r + j.r) and i.y - j.y <= (
                    i.r + j.r) and j.y - i.y <= (i.r + j.r) and not (i is j):
                c.move(i.repr, 1000, 1000)
                i.x += 1000
                i.y += 1000
                c.move(j.repr, 1000, 1000)
                j.x += 1000
                j.y += 1000
                cars.remove(i)
                mans.remove(j)
                Car()
                Man()
    for i in mans:
        i.mytick()
    c.after(10, tick)

root.title('BURUNDUK')
root.configure(background='green')
root.bind('<Key>', key)
tick()
root.mainloop()