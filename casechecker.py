import os

class CaseCheck:

    def __init__(self):

        self.coins  = 0
        self.kills = 0

    def coincollection(self,grid,Din):
        # for i in range(0,4,1):
        #     if(grid[Din.x + i][Din.y + 3] == '$'):
        #         self.coins+=1
        #         grid[Din.x + i][Din.y + 3] = ' '

        # for i in range(0,4,1):
        #     if(grid[Din.x+i][Din.y] == '$':
        #         self.coins+=1
        #         grid[Din.x + i][Din.y] = ' '

        for i in range(0,4,1):
            for j in range(0,4,1):
                if(grid[Din.x+i][Din.y + j] == '$'):
                    self.coins+=1
                    grid[Din.x + i][Din.y + j] = ' '



        