import os
import globalvariables as gv
import math
import time
from colorama import Fore,Back


#Creating a bullet class that will be used by both the Mandalorian as well as Viserion(the enemy dragon)
class Bullet():

    def __init__(self,x,y,grid):
        self.x = x
        self.y = y
        self.initialy = y
        self.initialx = x
        self.haveigoneup = 0
        self.bulletfigure = Fore.LIGHTYELLOW_EX + 'o' + '\x1b[0m'

    def bullet_vanished(self,grid):
        grid[self.x][math.floor(self.y)] = ' '

    def bullet_appears(self,grid):
        grid[self.x][math.floor(self.y)] = self.bulletfigure

    def bullet_move(self,grid):
        if self.y+2 < gv.MAX_Y:
            self.bullet_vanished(grid)
            self.y+=2
            self.bullet_appears(grid)
        
    def bullet_start(self,grid):
        
        if self.x > self.initialx - 20 and self.x > 1:
            self.bullet_vanished(grid)
            self.x-=1   
            self.haveigoneup+=1
            self.bullet_appears(grid)

    # A function to simulate gravity in the bullet...enables parabolic trajectory
    def bullet_gravity(self,grid):
        
        if self.x < 37:
            self.bullet_vanished(grid)
            self.x+=1
            self.bullet_appears(grid)
    

    # A function to check whether the bullet strikes anything or not
    def bullet_strike(self,grid):

        for i in range(2):
            for j in range(2):
                if self.y + j < 1000 and self.x + i < 40 and grid[self.x + i][self.y + j] == Back.LIGHTYELLOW_EX + '|' + '\x1b[0m':
                    grid[self.x + i][self.y + j] = ' '
                
                # if self.y + j < 1000 and self.x + i < 40 and grid[self.x + i][self.y + j] == Fore.YELLOW + '$' + '\x1b[0m':
                #     grid[self.x+i][self.y+j-1] = Fore.YELLOW + '$' + '\x1b[0m'

    def enemykill(self,grid,drogo):

        for j in range(10):
            if self.x == drogo.y + j:
                for i in range(8):
                    if self.y == drogo.x + i:
                        drogo.lives-=0.01 
                

class Ice(Bullet):

    def __init__(self,x,y,grid):
        Bullet.__init__(self, x, y, grid)
        self.bulletfigure = Back.CYAN + 'O' + '\x1b[0m'

    def ice_move(self,grid):
        self.bullet_vanished(grid)
        if self.y > 10:
            self.y-=5
        self.bullet_appears(grid)