from tkinter import *
from tkinter import colorchooser
import time
import random

class Cell(object):

    def __init__(self, canvas, x, y, d, life):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.d = d
        self.life = life
        self.nlife = life

    def predict(self, neigh):
        if (neigh==3 or(neigh==2 and self.life)):
            self.nlife = True
        else:
            self.nlife = False

    def refresh(self):
        self.life = self.nlife
        if self.life:
            color = 'blue'
        else:
            color = 'black'
        x = self.x
        y = self.y
        d = self.d
        self.canvas.create_rectangle(x, y, x+d, y+d,
                                     fill = color,
                                     outline = 'black')



class LifeCanvas(object):

    def __init__(self, root, canvas, w, h, n):
        self.root = root
        self.canvas = canvas
        self.w = int(w)
        self.h = int(h)
        self.n = int(n)
        self.d = int((1.0*self.w*self.h/self.n)**0.5)
        self.w = self.w - (self.w % self.d)
        self.h = self.h - (self.h % self.d)
        self.cellcanvas = [[Cell(canvas, x, y, self.d, random.choice([True, False]))
                            for y in range(0, self.h+1, self.d)]
                           for x in range(0, self.w+1, self.d)]

    def play(self):
        while True:
            for celllist in self.cellcanvas:
                for cell in celllist:
                    neigh = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if(self.cellcanvas[(cell.x//self.d+dx)%(self.w//self.d+1)]
                            [(cell.y//self.d+dy)%(self.h//self.d+1)].life and (dx != 0 or dy!=0)):
                                neigh+=1
                    cell.predict(neigh)
            for celllist in self.cellcanvas:
                for cell in celllist:
                    cell.refresh()
            self.root.update()
            self.canvas.delete("all")


n = input('Количество клеток на экране (рекомендуется использовать 1000-10000): ')
root = Tk()
screenw = root.winfo_screenwidth()
screenh = root.winfo_screenheight()
#root.attributes('-fullscreen', True) #может не работать на операционных системах, отличных от Windows
canvas = Canvas(root, width=screenw, height=screenh)
canvas.pack()
life = LifeCanvas(root, canvas, screenw, screenh, n)
life.play()