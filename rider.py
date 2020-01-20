from __future__ import print_function
import sys
import time
import os
import globalvariables as gv 
import math
from colorama import Back,Fore
from bullet import Bullet
import numpy as np


# Note: We use __ after many of the self.__ variables in order to keep them private


class Entity:

    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
 
class Rider(Entity):

    def __init__(self, x, y, grid):
        Entity.__init__(self, x, y, grid)
        self.__figure = [['_', '0', '_'], ['|', '-', '|'], ['|', '_', '|']]
        self.__dragonfigure1 = [['/','\\',' ',' ','/','\\',' ',' ','/','\\',' ',' ','O'],[' ',' ','\\','/',' ',' ','\\','/',' ',' ','\\','/',' ']]
        self.__dragonfigure2 = [[' ',' ','/','\\',' ',' ','/','\\',' ',' ','/','\\',' '],['\\','/',' ',' ','\\','/',' ',' ','\\','/',' ',' ','O']]
        self.__bulletlist = []
        self.shieldstatus = 0
        self.typestatus = 0
        self.setme = 0
        # self.__lives = gv.LIVES
       
    def initialplace(self,grid):
        if self.setme == 0:
            for i in range(35,38,1):
                for j in range(0,3,1):
                    grid[i][j] = self.__figure[i-35][j]

        else:
            for i in range(36,38,1):
                for j in range(0,13,1):
                    grid[i][j] = self.__dragonfigure1[i-36][j]

    def din_vanished(self,grid):
        if self.setme == 0:
            for i in range(self.x,self.x + 3):
                for j in range(self.y,self.y + 3):
                    grid[i][j] = " "
        else:
            for i in range(self.x,self.x + 2):
                for j in range(self.y,self.y + 13):
                    grid[i][j] = " "

    def din_appears(self,grid):
        if self.setme == 0:
            for i in range(self.x,self.x + 3):
                for j in range(self.y,self.y + 3):
                    grid[i][j] = self.__figure[i-self.x][j-self.y]
        else:
            for i in range(self.x,self.x + 2):
                for j in range(self.y,self.y + 13):
                    if np.mod(self.y,2)==0:
                        grid[i][j] = self.__dragonfigure1[i-self.x][j-self.y]
                    else:
                        grid[i][j] = self.__dragonfigure2[i-self.x][j-self.y]

    def din_move(self,grid,cin,Din):

        #Move to the right
        if(cin==1):
            if Din.y <=958:
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

    def bullethit(self,grid,drogo):
        for shot in self.__bulletlist:
            shot.bullet_move(grid)
            shot.bullet_strike(grid)
            shot.enemykill(grid,drogo)
            if shot.haveigoneup >= 0 and shot.haveigoneup <= 19:
                shot.bullet_start(grid)
            if shot.haveigoneup >= 19 or shot.x <= 1:
                shot.bullet_gravity(grid) 
            if(math.floor(shot.y - shot.initialy) == 150):
                shot.bullet_vanished(grid)
                self.__bulletlist.remove(shot)
            if shot.x == 37:
                shot.bullet_vanished(grid)
                self.__bulletlist.remove(shot)
            
    def activate_shield(self,grid):
        self.__figure = [[Fore.LIGHTRED_EX + '/', '0', '\\' + '\x1b[0m' ], [Fore.LIGHTRED_EX+'|', '-', '|'+'\x1b[0m'], [Fore.LIGHTRED_EX+ '|', '_', '|' +'\x1b[0m']]
        self.shieldstatus = 1

    def deactivate_shield(self,grid):
        self.__figure = [['_', '0', '_'], ['|', '-', '|'], ['|', '_', '|']]
        self.shieldstatus = 0


    def checkpowerup(self,setme):
        self.setme = setme