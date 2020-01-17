from __future__ import print_function
import os
import random
import globalvariables as gv 
import background
import surroundings
import rider 
import getinput
import time
import math
import signal
import datetime
import numpy as np 
from getinput import NBInput,keypress,clear
from colorama import init,Fore,Back
from surroundings import Surroundings
from bullet import Bullet
from casechecker import CaseCheck
from gameinit import GameInit
from viserion import Viserion
init()



board = background.Board(gv.MAX_X,gv.MAX_Y)
c =0
surr = Surroundings()
surr.create_ground(board.grid)
surr.create_sky(board.grid)
surr.create_coins(board.grid)
surr.create_clouds(board.grid,2,11)
surr.create_firebeam(board.grid)
surr.create_powerups(board.grid)
# surr.create_viserion(board.grid)
Din = rider.Rider(35, 0, 1)
Din.initialplace(board.grid)
drogo = Viserion(959,22,board.grid)
drogo.create_viserion(board.grid)
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

powercheck =0 
t = 0

#GAME LOOP
while True:

    print(' ')
    print(Fore.LIGHTGREEN_EX + "Coins: " + '\x1b[0m' + str(cases.coins) + Fore.LIGHTGREEN_EX + "  Lives: " + '\x1b[0m' + str(math.ceil(cases.lives)) ) 


    #For Screen Movement
    if c < 900:
        if(time.time() - y >= 0.1):
            y = time.time()
            if cases.gamespeedup(board.grid,Din) == 1:
                powercheck = 1
            if powercheck == 1:
                c+=3
            else:
                c+=1

    #Function to simulate gravity
    if(time.time() - z >= 0.05):
        z = time.time()
        cases.gravity(board.grid,Din)
      
    #Function to collect coins on the way during the game
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

    if c>=900:
        drogo.dragon_move(board.grid,Din)
    
    cases.boundaryconstraints(board.grid,c,Din)
    
    #Printing the screen and then clearing it up to reprint for the next instance of the gameplay
    print(board.draw_background(c))
    print('\033[H')

