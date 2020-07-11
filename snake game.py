import math
import pygame
import random
import tkinter as tk
from tkinter import messagebox
class cube(object):
    rows =0
    col =0
    def __init__(self,strt, dirx=1,diry=0,color=(255,0,0)):
        pass
    def move(self,dirx,diry):
        pass
    def draw(self,surface,eyes =False):
        pass
class snake(object):
    body = []
    turn = {}
    def __init__(self,color,pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirx =0
        self.diry =1
    def move(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if key[pygame.K_LEFT]:
                    self.dirx =-1
                    self.diry=0
                    self.turn[self.head.pos[:]] = [self.dirx,self.diry]
                elif key[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turn[self.head.pos[:]] = [self.dirx, self.diry]

                elif key[pygame.K_UP]:
                    self.dirx = -1
                    self.diry = 0
                    self.turn[self.head.pos[:]] = [self.dirx, self.diry]

                elif key[pygame.K_DOWN]:
                    self.dirx = 1
                    self.diry = 0
                    self.turn[self.head.pos[:]] = [self.dirx, self.diry]

        pass
    def reset(self,pos):
        pass
    def addcube(self):
        pass
    def draw(self,surface):
        pass

def drawgrid(w,rows,surface):
    size_btwn = w//rows
    x=0
    y=0
    for i in range(rows):
        x = x + size_btwn
        y = y + size_btwn
        pygame.draw.line(surface,white,(x,0),(x,w))
        pygame.draw.line(surface, white, (0, y), (w, y))


def redraw_window(surface):
    surface.fill((0,0,0))
    drawgrid(width,rows,surface)
    pygame.display.update()

def randon_snack(rows,items):
    pass

def message_box(subject,content):
    pass

def main():
    win = pygame.display.set_mode((width,width))
    color =(255,0,0)
    pos =(10,10)
    s = snake(color=color,pos=pos)
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(win)
    pass

width =500
rows = 20
white = (255,255,255)
main()