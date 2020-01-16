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
from colorama import init,Fore,Back
from bullet import Bullet
from casechecker import CaseCheck
init()



board = background.Board(gv.MAX_X,gv.MAX_Y)
surr = surroundings.Surroundings()
surr.create_ground(board.grid)
surr.create_sky(board.grid)
surr.create_coins(board.grid)
c = 0
surr.create_clouds(board.grid,2,11)
surr.create_firebeam(board.grid)
surr.create_viserion(board.grid)
Din = rider.Rider(35, 0, 1)
Din.initialplace(board.grid)
cases = CaseCheck()
# bullet = Bullet(10,0,board.grid)
keys = NBInput()
keys.nbTerm()
keys.flush()
y = time.time()
count = 0
z = time.time()
p = time.time()
print(board.draw_background(c))
print('\033[H')

t = 0

#GAME LOOP
while True:

    print(' ')
    print(Fore.LIGHTGREEN_EX + "Coins: " + '\x1b[0m' + str(cases.coins) + Fore.LIGHTGREEN_EX + "  Lives: " + '\x1b[0m' + str(cases.lives) ) 


    #For Screen Movement
    if(time.time() - y >= 0.1):
      y = time.time()
      c+=1

    if(time.time() - z >= 0.05):
        z = time.time()
        cases.gravity(board.grid,Din)
      
    cases.coincollection(board.grid,Din)
    

    #Checking for inputs and performing the required function
    input = ''
    if keys.kbHit():
        input = keys.getCh()
    
    cin = keypress(input)

    if cin:
        if cin in range(1,4,1):
            Din.din_move(board.grid,cin,Din)
        if cin == -1:
            clear()
            keys.orTerm()
            exit()
        if cin == 4:
            Din.shoot(Din,board.grid)
        if cin == 5:
            t = time.time()
            Din.activate_shield(board.grid)
            
    if(time.time()-t > 10):
        Din.deactivate_shield(board.grid)
    if(time.time()-p > 0.01):
        p = time.time()
        Din.bullethit(board.grid)


    
    if cases.beamcollision(board.grid,Din) == -1:
        clear()
        print("YOU HAVE LOST ALL YOUR LIVES")
        keys.orTerm()
        exit()

    # Function to simulate gravity 
    



    if(Din.y < c):
        Din.din_vanished(board.grid)
        Din.y = c
        Din.din_appears(board.grid)

    
    #Printing the screen and then clearing it up to reprint for the next instance of the gameplay
    print(board.draw_background(c))
    print('\033[H')

