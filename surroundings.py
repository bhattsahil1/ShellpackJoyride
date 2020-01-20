import os
import globalvariables as gv
import random
from colorama import Fore,Back

class Surroundings:

    def __init__(self):

        self.__ground = Fore.RED + '=' + '\x1b[0m'
        self.__sky = Fore.BLUE + '+' + '\x1b[0m'
        self.__firebeam = Back.LIGHTYELLOW_EX + '|' + '\x1b[0m'
        # self.__coins = Fore.YELLOW + '$' + '\x1b[0m'
        self.__powerup = Back.MAGENTA + "P" + '\x1b[0m'
        self.coindict = {}

    def create_ground(self,grid):
        for x in range(gv.MAX_Y):
            grid[gv.MAX_X-1][x]= self.__ground
            grid[gv.MAX_X-2][x] = Back.GREEN + ' ' + '\x1b[0m'

    def create_sky(self,grid):
        for x in range(gv.MAX_Y):
            grid[0][x] = self.__sky


    def create_coins(self,grid):
        for x in range(20):
            r = random.randint(1,900)
            xais = random.randint(10,34)
            for i in range(r,r+10):
                self.coindict[i] = xais
                # grid[xais][i] = self.__coins
        return self.coindict

    def create_powerups(self,grid):

        for x in range(10):
            r = random.randint(3,34)
            yais = random.randint(5,900)
            grid[r][yais] = self.__powerup

    def create_firebeam(self,grid):

        for x in range(4):
            r = random.randint(8,28)
            yais = random.randint(10,900)
            diff = yais - r
            for i in range(r,r+8):
                grid[i][i+diff] = self.__firebeam
            
            r = random.randint(10,29)
            yais = random.randint(10,900)
            for i in range(r,r+7):
                grid[i][yais] = self.__firebeam
            
            r = random.randint(10,29)
            yais = random.randint(10,900)
            for i in range(yais,yais+15):
                grid[r][i] = self.__firebeam

    def create_magnet(self,grid):

        for x in range(3):
            yais = random.randint(100,700)
            for y in range(yais,yais+10):
                grid[10][y] = 'M'
    
    def create_drogonpowerup(self,grid):

        r = random.randint(10,30)
        yais = random.randint(250,650)
        for x in range(2):
            for y in range(2):
                grid[r+x][yais+y] = Back.LIGHTWHITE_EX + 'D' + '\x1b[0m'
        

class Coin:

    def __init__(self):
        self.coinstatus = 0
        self.coinfigure = Fore.YELLOW + '$' + '\x1b[0m'
    
    def coin_render(self,coindict,grid):
        for i in coindict:
            grid[coindict[i]][i] = self.coinfigure

