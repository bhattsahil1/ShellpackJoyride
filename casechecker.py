import os
from colorama import Fore,Back
import time
import globalvariables as gv

class CaseCheck:

    def __init__(self):

        self.coins  = 0
        self.kills = 0
        self.lives = gv.LIVES

    def coincollection(self,grid,Din):
        for i in range(0,4,1):
            for j in range(0,4,1):
                if(grid[Din.x+i][Din.y + j] == Fore.YELLOW + '$' + '\x1b[0m'):
                    self.coins+=1
                    grid[Din.x + i][Din.y + j] = ' '

    def gravity(self,grid,Din):
        if(Din.x != 35):
            Din.din_vanished(grid)
            Din.x+=1
            Din.din_appears(grid)
            # time.sleep(0.05)

    def beamcollision(self,grid,Din):
        for i in range(0,4,1):
            for j in range(0,4,1):
                if(grid[Din.x+i][Din.y + j] == Back.LIGHTYELLOW_EX + '|' + '\x1b[0m'):
                    self.lives-=0.2
                    grid[Din.x + i][Din.y + j] = ' '
                    if self.lives == 0:
                        return -1
        return 1
    
    def gamespeedup(self,grid,Din):
        for i in range(0,4,1):
            for j in range(0,4,1):
                if(grid[Din.x+i][Din.y + j] ==  Back.MAGENTA + "P" + '\x1b[0m'):
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
        
         


        