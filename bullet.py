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
        self.initialx = x
        self.haveigoneup = 0
        self.__bulletfigure = Fore.LIGHTYELLOW_EX + 'o' + '\x1b[0m'

    def bullet_vanished(self,grid):
        grid[self.x][math.floor(self.y)] = ' '

    def bullet_appears(self,grid):
        grid[self.x][math.floor(self.y)] = self.__bulletfigure

    def bullet_move(self,grid):
        if self.y+2 < gv.MAX_Y:
            self.bullet_vanished(grid)
            self.y+=2
            self.bullet_appears(grid)
        
    def bullet_start(self,grid):
        
        if self.x > self.initialx - 20 and self.x > 1:
            self.bullet_vanished(grid)
            self.x-=1   
            self.haveigoneup+=1
            self.bullet_appears(grid)
        # print(self.haveigoneup)

    def bullet_gravity(self,grid):
        
        if self.x < 37:
            self.bullet_vanished(grid)
            self.x+=1
            self.bullet_appears(grid)
            # time.sleep(0.05)
    
    def bullet_strike(self,grid):

        for i in range(2):
            for j in range(2):
                if self.y + j < 1000 and self.x + i < 40 and grid[self.x + i][self.y + j] == Back.LIGHTYELLOW_EX + '|' + '\x1b[0m':
                    grid[self.x + i][self.y + j] = ' '
                
                if self.y + j < 1000 and self.x + i < 40 and grid[self.x + i][self.y + j] == Fore.YELLOW + '$' + '\x1b[0m':
                    grid[self.x+i][self.y+j-1] = Fore.YELLOW + '$' + '\x1b[0m'
                
