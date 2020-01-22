import os
import globalvariables as gv
import random
from colorama import Fore,Back

class Surroundings:

    def __init__(self):

        self.__ground = gv.Ground
        self.__sky = gv.Sky
        self.__powerup = gv.Powerup
        self.coindict = {}

    def create_ground(self,grid):
        for x in range(gv.MAX_Y):
            grid[gv.MAX_X-1][x]= self.__ground
            grid[gv.MAX_X-2][x] = gv.Grass

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
        poweruplist = []
        for x in range(10):
            r = random.randint(3,34)
            yais = random.randint(5,900)
            poweruplist.append((r,yais))
        return poweruplist
            # grid[r][yais] = self.__powerup

    def create_firebeam(self,grid):

        masterlist = []
        
        for x in range(8):
            #Diagonal beams
            r = random.randint(8,23)
            yais = random.randint(10,900)
            diff = yais - r
            a = []
            for i in range(r,r+14):
                a.append((i,i+diff))
            masterlist.append(a)
            
            b = []
            #Vertical beams
            r = random.randint(10,24)
            yais = random.randint(10,900)
            for i in range(r,r+13):
                b.append((i,yais))
            masterlist.append(b)
            
            c = []
            #Horizontal beams
            r = random.randint(10,29)
            yais = random.randint(10,900)
            for i in range(yais,yais+15):
                c.append((r,i))
            masterlist.append(c)
            
        return masterlist

    def create_magnet(self,grid):
        magnetlist = []
        for x in range(2):
            yais = random.randint(100,700)
            xais = random.randint(10,32)
            magnetlist.append((xais,yais))
        return magnetlist
    
    def create_drogonpowerup(self,grid):

        r = random.randint(10,30)
        yais = random.randint(250,650)
        for x in range(2):
            for y in range(2):
                grid[r+x][yais+y] = gv.DragonPowerUp
        

class Coin:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.coinstatus = 0
        self.__coinfigure = gv.Coin
    
    def coin_render(self,coindict,grid):
        for i in coindict:
            grid[coindict[i]][i] = self.__coinfigure
         

class Firebeam:

    def __init__(self,coordinatelist):
        self.coordinatelist = coordinatelist
        self.__beamfigure = Back.LIGHTYELLOW_EX + '|' + '\x1b[0m'

    def display_beam(self,grid):
        for x in self.coordinatelist:
            grid[x[0]][x[1]] = self.__beamfigure
        
    def destroy_beam(self):
        self.__beamfigure = ' '

class Magnet:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.__magnetfigure = Back.RED + 'M' + '\x1b[0m'

    def display_magnet(self,grid):
        for i in range(self.x,self.x+5,1):
            grid[i][self.y] = self.__magnetfigure
    
class PowerUp:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.__powerfigure = gv.Powerup

    def display_powerup(self,poweruplist,grid):
        for i in poweruplist:
            grid[i[0]][i[1]] = self.__powerfigure