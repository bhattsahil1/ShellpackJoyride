import os
import globalvariables as gv
import random
from colorama import Back

class Surroundings:

    def __init__(self):

        self.__ground = '='
        self.__sky = '+'
        self.__cloud = []

    def create_ground(self,grid):
        for x in range(gv.MAX_Y):
            grid[gv.MAX_X-1][x]= self.__ground
            grid[gv.MAX_X-2][x] = ' '

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

