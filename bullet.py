import os
import globalvariables as gv
import math
import time
from colorama import Fore,Back


#Creating a bullet class that will be used by both the Mandalorian as well as Viserion(the enemy dragon)
class Bullet():

    def __init__(self,x,y,grid):
        self.__initialy = y
        self.__initialx = x
        self.x = x
        self.y = y
        self.__haveigoneup = 0
        self.bulletfigure = gv.Bullet

    def bullet_vanished(self,grid):
        grid[self.x][math.floor(self.y)] = ' '

    def bullet_appears(self,grid):
        grid[self.x][math.floor(self.y)] = self.bulletfigure

    def bullet_move(self,grid):
        if self.y+2 < gv.MAX_Y:
            self.bullet_vanished(grid)
            self.y+=2
            self.bullet_appears(grid)
        
    def bullet_start(self,grid):
        
        if self.x > self.__initialx - 20 and self.x > 1:
            self.bullet_vanished(grid)
            self.x-=1   
            self.__haveigoneup+=1
            self.bullet_appears(grid)

    # A function to simulate gravity in the bullet...enables parabolic trajectory
    def bullet_gravity(self,grid):
        
        if self.x < 37:
            self.bullet_vanished(grid)
            self.x+=1
            self.bullet_appears(grid)
    

    # A function to check whether the bullet strikes anything or not
    def bullet_strike(self,grid,masterlist):

        for i in range(2):
            for j in range(2):
                if self.y + j < 1000 and self.x + i < 40 and grid[self.x + i][self.y + j] == gv.Obstacle:
                    tup = (self.x+i,self.y+j)
                    for x in masterlist:
                        if tup in x:
                            return masterlist.index(x)
                    grid[self.x + i][self.y + j] = ' '
        return -1
    def enemykill(self,grid,drogo):

        for j in range(10):
            if self.x == drogo.y + j:
                for i in range(8):
                    if self.y == drogo.x + i:
                        drogo.lives-=0.01 
    
    def bulletgetter(self):
        coordlist = []
        coordlist.append(self.x)
        coordlist.append(self.y)
        coordlist.append(self.__initialx)
        coordlist.append(self.__initialy)
        coordlist.append(self.__haveigoneup)
        return coordlist

class Ice(Bullet):

    def __init__(self,x,y,grid):
        Bullet.__init__(self, x, y, grid)
        self.x = x
        self.y = y
        self.bulletfigure =gv.Iceball

    def ice_move(self,grid):
        self.bullet_vanished(grid)
        if self.y > 10:
            self.y-=5
        self.bullet_appears(grid)

    def sendcoods(self):
        cood = []
        cood.append(self.x)
        cood.append(self.y)
        return cood