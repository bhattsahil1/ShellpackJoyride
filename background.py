import numpy as np
import os
import globalvariables as gv
from colorama import Fore,Back


class Board:

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = columns
        self.__coins = 0
        self.grid = []

        # self.grid = np.array([[' ' for col in range(gv.MAX_Y)]for row in range(rows)])
        # self.grid = [[' ' for col in range(gv.MAX_Y)]for row in range(rows)]   
        
        for i in range(self.__rows):
            self.new = []
            for j in range(gv.MAX_Y):
                self.new.append(" ")
            self.grid.append(self.new)
        self.startfrom = 0

    def draw_background(self,c):
        strBoard = ""

        for row in self.grid:
            strBoard += ''.join(row[c:c+150]) + '\n'
        return strBoard
    
    def clear_background(self,c):
        strBoard = ""
        clearlist = []
        for x in range(gv.MAX_Y):
            clearlist.append(' ')
        for row in self.grid:
            strBoard += ''.join(clearlist[c:c + 150]) + '\n'
        return strBoard
