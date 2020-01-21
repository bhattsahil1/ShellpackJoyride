from rider import Entity
import os
from colorama import Back,Fore
import globalvariables as gv
from bullet import Ice

class Viserion(Entity):

    def __init__(self,x,y,grid):
        Entity.__init__(self, x, y, grid)
        self.__dragon = []
        self.__iceballs = []
        self.lives = 5
        self.__blanklist = []
    
    def positionalfunction(self,grid,somelist):
        var1 = self.x
        var2 = self.y
        x = var2
        y = var1 
        for i in range(15):
            for j in range(39):
                grid[x][y] = somelist[i][j]
                y+=1
            y=var1
            x+=1
 
    def create_viserion(self,grid):

        with open("dragon.txt") as obj:
            for line in obj:
                self.__dragon.append(line.strip('\n'))
        
        for i in range(15):
            newlist = []
            for j in range(39):
                newlist.append(' ')
            self.__blanklist.append(newlist)


        self.positionalfunction(grid,self.__dragon)



    def dragon_vanished(self,grid):
        self.positionalfunction(grid,self.__blanklist)



    def dragon_appears(self,grid):
        self.positionalfunction(grid,self.__dragon)



    def dragon_move(self,grid,Din):
        self.dragon_vanished(grid)
        self.y = 22 - (35 - Din.x)
        if self.y <=1 :
            self.y = 2
        self.dragon_appears(grid)
    
    def dragon_appu(self,grid,Din):
        self.__iceballs.append(Ice(Din.x,957,grid))
        

    def dragon_attack(self,grid,Din):
        for shot in self.__iceballs:
            shot.ice_move(grid)
            a = shot.sendcoods()
            if(a[1] <=902):
                shot.bullet_vanished(grid)
                self.__iceballs.remove(shot)
            for i in range(5):
                for j in range(5):
                    if a[0] == Din.x + i and a[1] == Din.y + j:
                        return 1
        return -1
        


