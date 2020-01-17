from rider import Entity
import os
from colorama import Back,Fore
import globalvariables as gv

959,22
class Viserion(Entity):

    def __init__(self,x,y,grid):
        Entity.__init__(self, x, y, grid)
        self.__dragon = []
    
    def create_viserion(self,grid):

        with open("dragon.txt") as obj:
            for line in obj:
                self.__dragon.append(line.strip('\n'))

        e = self.x
        f = self.y
        c = f
        d = e 
        for i in range(15):
            for j in range(39):
                grid[c][d] = self.__dragon[i][j]
                d+=1
            d=e
            c+=1

    def dragon_vanished(self,grid):
        e = self.x 
        f = self.y 
        c = f
        d = e 
        for i in range(15):
            for j in range(39):
                grid[c][d] = ' '
                d+=1
            d=e
            c+=1
    def dragon_appears(self,grid):
        e = self.x 
        f = self.y 
        c = f
        d = e
        for i in range(15):
            for j in range(39):
                grid[c][d] = self.__dragon[i][j]
                d+=1
            d=e
            c+=1
    
    def dragon_move(self,grid,Din):
        self.dragon_vanished(grid)
        self.y = 22 - (35 - Din.x)
        if self.y <=1 :
            self.y = 2
        self.dragon_appears(grid)


