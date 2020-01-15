from __future__ import print_function
import sys
import time
import os
import globalvariables as gv 
import math
from colorama import Back,Fore
from bullet import Bullet


# Note: We use __ after many of the self.__ variables in order to keep them private


class Entity:

    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
 
class Rider(Entity):

    def __init__(self, x, y, grid):
        Entity.__init__(self, x, y, grid)
        self.__figure = [['_', '0', '_'], ['|', '-', '|'], ['|', '_', '|']]
        self.__bulletlist = []
        # self.__lives = gv.LIVES
       
    def initialplace(self,grid):
        for i in range(35,38,1):
            for j in range(0,3,1):
                grid[i][j] = self.__figure[i-35][j]

    def din_vanished(self,grid):
        for i in range(self.x,self.x + 3):
            for j in range(self.y,self.y + 3):
                grid[i][j] = " "

    def din_appears(self,grid):
        for i in range(self.x,self.x + 3):
            for j in range(self.y,self.y + 3):
                grid[i][j] = self.__figure[i-self.x][j-self.y]

    def din_move(self,grid,cin,Din):

        #Move to the right
        if(cin==1):
            Din.din_vanished(grid)
            Din.y+=1
            Din.din_appears(grid)

        #Move to the left
        if(cin == 2):
            Din.din_vanished(grid)
            Din.y-=1
            Din.din_appears(grid)
        
        #Move upwards
        if(cin == 3):
            Din.din_vanished(grid)
            if(Din.x-10 <= 0):
                Din.x = 1
            else:
                Din.x-=10
            Din.din_appears(grid)

    def shoot(self,Din,grid):
        self.__bulletlist.append(Bullet(Din.x + 1,Din.y + 4,grid))

    def bullethit(self,grid):
        for shot in self.__bulletlist:
            shot.bullet_move(grid)
            if(math.floor(shot.y - shot.initialy) == 50):
                shot.bullet_vanished(grid)
                self.__bulletlist.remove(shot)
            