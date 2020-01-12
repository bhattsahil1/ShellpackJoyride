from __future__ import print_function
import sys
import time
import os
from colorama import Back

class Entity:

    def __init__(self, x, y, grid):
        self.x = x
        self.y = y


class Rider(Entity):

    def __init__(self, x, y, grid):
        Entity.__init__(self, x, y, grid)
        self.__figure = [[" ", '_', '0', '_', " "], ['/', "\\", '-', '/', "\\"], [" ", '/', '|', '\\', " "]]
        # USING the __ after self tp ensure the variables are private and cannot be accessed outside
    
    def initialplace(self,grid):
        for i in range(35,38,1):
            for j in range(0,5,1):
                grid[i][j] = self.__figure[i-35][j]

    def din_vanished(self,grid):
        for i in range(self.x,self.x + 3):
            for j in range(self.y,self.y + 5):
                grid[i][j] = " "

    def din_appears(self,grid):
        for i in range(self.x,self.x + 3):
            for j in range(self.y,self.y + 5):
                grid[i][j] = self.__figure[i-self.x][j-self.y]