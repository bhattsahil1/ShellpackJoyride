from __future__ import print_function
import os
import random
import globalvariables as gv 
import background
import surroundings
import rider 
import getinput
import time
import signal
import datetime
# from getinput import _getChUnix as getChar
import numpy as np 
from getinput import NBInput,keypress,clear

class AlarmException(Exception):
    '''This class executes the alarmexception.'''
    pass


board = background.Board(gv.MAX_X,gv.MAX_Y)
surr = surroundings.Surroundings()
surr.create_ground(board.grid)
surr.create_sky(board.grid)
c = 0
surr.create_clouds(board.grid,2,11)
# board.draw_background(c)

# x = time.time()
# y = x
Din = rider.Rider(35, 0, 1)
Din.initialplace(board.grid)

# def movedin(Din,grid):
#     def alarmhandler(signum, frame):
#         raise AlarmException
    
#     def user_input(timeout=0.75):
#         signal.signal(signal.SIGALRM,alarmhandler)
#         signal.setitimer(signal.ITIMER_REAL,timeout)

#         try:
#             text = getChar()()
#             signal.alarm
#             return text
#         except AlarmException:
#             pass
#         signal.signal(signal.SIGALRM,signal.SIG_IGN)
#         return ''

#     char = user_input()

#     if(char=='d'):
#         Din.din_vanished(grid)
#         Din.y+=10
#         Din.din_appears(grid)

#     if(char=='a'):
#         Din.din_vanished(grid)
#         Din.y-=10
#         Din.din_appears(grid)
#     if(char=='w'):
#         Din.din_vanished(grid)
#         Din.x -=2
#         Din.din_appears(grid)

# z = x
keys = NBInput()
keys.nbTerm()
keys.flush()
# keys.getCh()
# x = datetime.datetime.now()
# y = x
y = time.time()
while True:
    # os.system('clear')
    clear()
    if(time.time() - y >= 0.1):
      y = time.time()
      c+=1


    # Din.din_vanished(board.grid)
    # Din.y+=1
    # Din.din_appears(board.grid)
    
    input = ''
    if keys.kbHit():
        input = keys.getCh()
    
    cin = keypress(input)

    if cin:
        if(cin == 1):
            Din.din_vanished(board.grid)
            Din.y+=10
            Din.din_appears(board.grid)

        if(cin == 2):
            Din.din_vanished(board.grid)
            Din.y-=10
            Din.din_appears(board.grid)

        if(cin == 3):
            Din.din_vanished(board.grid)
            if(Din.x-10 <= 0):
                Din.x = 1
            else:
                Din.x-=10
            Din.din_appears(board.grid)
        if(cin == -1):
            clear()
            keys.orTerm()
            exit()

        if(Din.x != 35):
            Din.din_vanished(board.grid)
            Din.x+=1
            Din.din_appears(board.grid)
        # time.sleep(0.1)
    board.draw_background(c)


