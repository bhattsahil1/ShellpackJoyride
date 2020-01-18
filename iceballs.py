import os
import globalvariables as gv
import math
import time
from colorama import Fore,Back

class Ice():

    def __init__(self,x,y,grid):
        self.x = x
        self.y = y
        self.initialy = y
        self.initialx = x
        self.haveigoneup = 0
        self.__icefigure = Fore.CYAN + 'O' + '\x1b[0m'

    def ice_vanished(self,grid):
        grid[self.x][self.y] = ' '

    def ice_appears(self,grid):
        grid[self.x][self.y] = self.__icefigure

    def ice_move(self,grid):
        self.ice_vanished(grid)
        self.y-=5
        self.ice_appears(grid)
                