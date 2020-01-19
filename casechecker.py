import os
from colorama import Fore,Back
import time
import globalvariables as gv
import math

class CaseCheck:

    def __init__(self):

        self.coins  = 0
        self.kills = 0
        self.lives = gv.LIVES

    def coincollection(self,grid,Din):
        for i in range(5):
            for j in range(5):
                if grid[Din.x+i][Din.y+j] == Fore.YELLOW + '$' + '\x1b[0m':
                    self.coins+=1
                    grid[Din.x+i][Din.y + j] = ' '

    def gravity(self,grid,Din):
        if(Din.x != 35):
            Din.din_vanished(grid)
            Din.x+=1
            Din.din_appears(grid)

    def beamcollision(self,grid,Din):
        for i in range(0,5,1):
            for j in range(0,5,1):
                if(grid[Din.x + i][Din.y + j] == Back.LIGHTYELLOW_EX + '|' + '\x1b[0m' and getattr(Din,'shieldstatus') == 0):
                    self.lives-=0.2
                    grid[Din.x + i][Din.y + j] = ' '
                    if math.floor(self.lives) == 0:
                        return -1
        return 1
    
    def gamespeedup(self,grid,Din):
        for i in range(0,5,1):
            for j in range(0,5,1):
                if(grid[Din.x + i][Din.y + j] ==  Back.MAGENTA + "P" + '\x1b[0m'):
                    grid[Din.x + i][Din.y + j] = ' '
                    return 1
        return -1
    
    def boundaryconstraints(self,grid,c,Din):
        if(Din.y < c):
            Din.din_vanished(grid)
            Din.y = c
            Din.din_appears(grid)
        if(Din.y >= c + 147):
            Din.din_vanished(grid)
            Din.y = c + 147
            Din.din_appears(grid)
    
    def magnet(self,grid,Din):
        if grid[10][Din.y+3] == 'M' or grid[10][Din.y+2] == 'M' or grid[10][Din.y+1] == 'M' or grid[10][Din.y] == 'M':
            if Din.x >16: 
                Din.din_vanished(grid)
                Din.x-=5
                Din.din_appears(grid)
            if Din.x < 6:
                Din.din_vanished(grid)
                Din.x+=1
                Din.din_appears(grid)
        

        