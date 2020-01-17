from rider import Entity
import os
from colorama import Back,Fore
import globalvariables as gv
from iceballs import Ice

# 959,22
class Viserion(Entity):

    def __init__(self,x,y,grid):
        Entity.__init__(self, x, y, grid)
        self.__dragon = []
        self.__iceballs = []
    
    def create_viserion(self,grid):

        with open("dragon.txt") as obj:
            for line in obj:
                self.__dragon.append(Fore.LIGHTGREEN_EX + line.strip('\n') + '\x1b[0m')

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
    
    def dragon_appu(self,grid,Din):
        self.__iceballs.append(Ice(Din.x,957,grid))
        # print(self.__iceballs)
        

    def dragon_attack(self,grid,Din):
        for shot in self.__iceballs:
            shot.ice_move(grid)
            if(shot.y <=902):
                shot.ice_vanished(grid)
                self.__iceballs.remove(shot)


