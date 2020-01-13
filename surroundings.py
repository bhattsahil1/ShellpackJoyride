import os
import globalvariables as gv
import random
from colorama import Fore,Back

class Surroundings:

    def __init__(self):

        self.__ground = Fore.RED + '=' + '\x1b[0m'
        self.__sky = Fore.BLUE + '+' + '\x1b[0m'
        self.__cloud = []
        self.__firebeam = Back.LIGHTYELLOW_EX + '|' + '\x1b[0m'
        self.__coins = Fore.YELLOW + '$' + '\x1b[0m'

    def create_ground(self,grid):
        for x in range(gv.MAX_Y):
            grid[gv.MAX_X-1][x]= self.__ground
            grid[gv.MAX_X-2][x] = Back.GREEN + ' ' + '\x1b[0m'

    def create_sky(self,grid):
        for x in range(gv.MAX_Y):
            grid[0][x] = self.__sky
        

    def create_clouds(self,grid,c,d):
        with open("cloud3.txt") as obj:
            for line in obj:
                self.__cloud.append(line.strip('\n'))
        
        while(d<800):
            e = d
            f = c
            for i in range(4):
                for j in range(16):
                    grid[c][d] = self.__cloud[i][j]
                    d+=1
                d=e
                c+=1
            c = f + random.randint(0,2)
            d += 37 + random.randint(10,50)

    def create_coins(self,grid):
        for i in range(20,25):
            grid[20][i] = self.__coins
        for i in range(50,55):
            grid[30][i] = self.__coins
        for i in range(120,125):
            grid[25][i] =  self.__coins
            grid[24][i] = self.__coins

        for i in range(200,205):
            grid[37][i] = self.__coins

    

    def create_firebeam(self,grid):

        for i in range(10,15):
            for j in range(40,45):
                if( i+30 == j):
                    grid[i][j] = self.__firebeam
                
        for i in range(28,33):
            grid[i][130] = self.__firebeam

        for i in range(250,260):
            grid[33][i] = self.__firebeam