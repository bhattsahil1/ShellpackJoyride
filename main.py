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
import numpy as np 
from getinput import NBInput,keypress,clear
from colorama import init
from casechecker import CaseCheck

init()
board = background.Board(gv.MAX_X,gv.MAX_Y)
surr = surroundings.Surroundings()
surr.create_ground(board.grid)
surr.create_sky(board.grid)
surr.create_coins(board.grid)
c = 0
surr.create_clouds(board.grid,2,11)

Din = rider.Rider(35, 0, 1)
Din.initialplace(board.grid)
cases = CaseCheck()

keys = NBInput()
keys.nbTerm()
keys.flush()
y = time.time()
count = 0
while True:
    # os.system('clear')
    if(time.time() - y >= 0.1):
      y = time.time()
      c+=1
      
    cases.coincollection(board.grid,Din)
    
    input = ''
    if keys.kbHit():
        input = keys.getCh()
    
    cin = keypress(input)

    if cin:
        if(cin == 1):
            Din.din_vanished(board.grid)
            Din.y+=1
            Din.din_appears(board.grid)

        if(cin == 2):
            Din.din_vanished(board.grid)
            Din.y-=1
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
    if(Din.y < c):
        Din.din_vanished(board.grid)
        Din.y = c
        Din.din_appears(board.grid)

    if(Din.x != 35):
        Din.din_vanished(board.grid)
        Din.x+=1
        Din.din_appears(board.grid)
        time.sleep(0.05)
    print(board.draw_background(c))
    print("Coins: " + str(cases.coins)) 
    print('\033[H')

