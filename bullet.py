import os
import globalvariables as gv
import math
# from rider import Entity
import time
from colorama import Fore,Back

class Bullet():

    def __init__(self,x,y,grid):
        # Entity.__init__(self, x, y, grid)
        self.x = x
        self.y = y
        self.initialy = y
        self.__bulletfigure = Fore.LIGHTYELLOW_EX + 'o' + '\x1b[0m'
    
    def bullet_vanished(self,grid):
        grid[self.x][math.floor(self.y)] = ' '

    def bullet_appears(self,grid):
        grid[self.x][math.floor(self.y)] = self.__bulletfigure

    def bullet_move(self,grid):
        if self.y+0.05 < gv.MAX_Y:
            self.bullet_vanished(grid)
            self.y+=0.05
            self.bullet_appears(grid)
        