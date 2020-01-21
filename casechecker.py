import os
from colorama import Fore,Back
import time
import globalvariables as gv
import math

class CaseCheck:

    def __init__(self):

        self.coins  = 0
        self.__lives = gv.LIVES

    def coincollection(self,grid,Din,coindict):
        for i in range(5):
            for j in range(5):
                if grid[Din.x+i][Din.y+j] == gv.Coin:
                    try:
                        del coindict[Din.y + j]
                        self.coins+=1
                    except KeyError:
                        pass
        return coindict

    def gravity(self,grid,Din):
        if(Din.x != 35):
            Din.din_vanished(grid)
            Din.x+=1
            Din.din_appears(grid)

    def beamcollision(self,grid,Din,masterlist):
        for i in range(0,5,1):
            for j in range(0,5,1):
                if(grid[Din.x + i][Din.y + j] == gv.Obstacle and Din.getshieldstatus() == 0):
                    self.__lives-=1
                    tup = (Din.x+i,Din.y+j)
                    for x in masterlist:
                        if tup in x:
                            return masterlist.index(x)
                    grid[Din.x + i][Din.y + j] = ' '
        return -1
    
    def livescheck(self,grid,Din):
        if math.floor(self.__lives) ==0:
            return -1
        return 1


    def gamespeedup(self,grid,Din):
        for i in range(0,5,1):
            for j in range(0,5,1):
                if(grid[Din.x + i][Din.y + j] ==  gv.Powerup):
                    grid[Din.x + i][Din.y + j] = ' '
                    return 1
        for i in range(2):
            for j in range(2):
                if Din.x - i >= 2 and Din.y - j >=2 and (grid[Din.x-i][Din.y-j]== gv.Powerup or grid[Din.x-i][Din.y+j]== gv.Powerup) :
                    grid[Din.x - i][Din.y - j] = ' '
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
    
    def magnet(self,grid,Din,c):
        m = 0
        for i in range(150):
            if Din.y + i < c + 150 and grid[Din.x][Din.y+i] == gv.Magnet:
                m = Din.y + i
        if Din.y < m:
            Din.din_vanished(grid)
            Din.y+=3
            Din.x-=1
            Din.din_appears(grid)
        
    def drogopowerup(self,grid,Din):
        for i in range(0,5,1):
            for j in range(0,5,1):
                if grid[Din.x + i][Din.y + j] == gv.DragonPowerUp:
                    return 1
        return -1       

    def returnlives(self):
        return self.__lives
        
    def reducelife(self):
        self.__lives-=1