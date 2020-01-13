import os
# from rider import Entity
from colorama import Fore,Back

class Bullet():

    def __init__(self,x,y,grid):
        # Entity.__init__(self, x, y, grid)
        self.x = x
        self.y = y
        self.__bulletfigure = Fore.LIGHTYELLOW_EX + 'o' + '\x1b[0m'
    


    def bullet_vanished(self,grid):
        grid[self.x][self.y] = ' '

    def bullet_appears(self,grid): 
        grid[self.x][self.y] = self.__bulletfigure

    def bullet_move(self,grid):
        self.bullet_vanished(grid)
        self.y+=10
        self.bullet_appears(grid)
        