import numpy as np
import os
import globalvariables as gv
from colorama import Fore,Back


class Board:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns

        self.grid = np.array([[' ' for col in range(gv.MAX_Y)]for row in range(rows)])
        self.grid = [[' ' for col in range(gv.MAX_Y)]for row in range(rows)]   
        self.startfrom = 0

    def draw_background(self,c):

        for i in range(self.rows):
            for j in range(c,c+200,1):
                print(self.grid[i][j],end='')
            print()
