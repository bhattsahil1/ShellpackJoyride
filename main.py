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
import subprocess
from colorama import init,Fore,Back
from surroundings import Surroundings,Coin
from bullet import Bullet
from casechecker import CaseCheck
from gameinit import GameInit
from viserion import Viserion
import printfunctions

#Remove this later
import pygame

init()

#Setting up the board
board = background.Board(gv.MAX_X,gv.MAX_Y)
c =0

#Setting the surroundings for the game
surr = Surroundings()
surr.create_ground(board.grid)
surr.create_sky(board.grid)
coinsdict = surr.create_coins(board.grid)
surr.create_firebeam(board.grid)
surr.create_powerups(board.grid)
surr.create_magnet(board.grid)
surr.create_drogonpowerup(board.grid)

#Setting up the Mandalorian and Viserion
Din = rider.Rider(35, 0, 1)
Din.initialplace(board.grid)

drogo = Viserion(959,22,board.grid)
drogo.create_viserion(board.grid)

#Initializing variables that will be used across the game loop
cases = CaseCheck()
keys = NBInput()
keys.nbTerm()
keys.flush()

y = time.time()
count = 0
z = time.time()
p = time.time()

checktime = 0
powercheck =0 
t = 0
f = 0
dragonballreload = 0
dragonshootdelay = 0
endgametime = 0
timeleft = 1000
setme = 0

display = printfunctions.PrintMe(1)
display.title()

#Remove this later
pygame.init()
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.play(-1)

#coins
paisa = Coin()


os.system('clear')
print(board.draw_background(c))
print('\033[H')

print(' ')
#GAME LOOP
while True:

    #Preparing the top bar for displaying scores,lives,time left etc.
    if c < 900:
        print(Fore.LIGHTGREEN_EX + "Coins: " + '\x1b[0m' + str(cases.coins) + Fore.LIGHTGREEN_EX + "  Lives: " + '\x1b[0m' + str(math.ceil(cases.lives)) + ' ' + Fore.LIGHTGREEN_EX + "Enemy Lives: " + '\x1b[0m' + str(math.ceil(drogo.lives)) )  
    else:
        print(Fore.LIGHTGREEN_EX + "Coins: " + '\x1b[0m' + str(cases.coins) + Fore.LIGHTGREEN_EX + "  Lives: " + '\x1b[0m' + str(math.ceil(cases.lives)) + ' ' + Fore.LIGHTGREEN_EX + "Enemy Lives: " + '\x1b[0m' + str(math.ceil(drogo.lives)) + ' ' + Fore.LIGHTGREEN_EX + "TIME REMAINING: " + '\x1b[0m' + str(math.ceil(timeleft)) )  

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
    coinsdict = cases.coincollection(board.grid,Din,coinsdict)
    

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
            if time.time() - checktime > 30:
                t = time.time()
                Din.activate_shield(board.grid)
                checktime = time.time()


    #Deactivating shield after 10s        
    if(time.time()-t > 10):
        Din.deactivate_shield(board.grid)

    #Constantly firing bullets that are appended to the Mando's bulletlist
    if(time.time()-p > 0.01):
        p = time.time()
        Din.bullethit(board.grid,drogo)



    #Exiting the game in case all lives are lost or if the Mandalorian wins
    if math.ceil(cases.lives) == 0 or math.ceil(timeleft) == 0:
        clear()
        display.losingscenario()
        keys.orTerm()
        exit()

    if math.ceil(drogo.lives) == 0:
        clear()
        display.winningscenario()
        keys.orTerm()
        exit()

    #Setting up the time counter for the final fight
    if c<900:
        endgametime = time.time()

    #The Viserion Final Fight section !
    if c>=900:
        timeleft = 30 -(time.time()-endgametime)
        drogo.dragon_move(board.grid,Din)
        if time.time() - dragonballreload >= 1 :
            drogo.dragon_appu(board.grid,Din)
            dragonballreload = time.time()
        if time.time() - dragonshootdelay >= 0.1:
            if drogo.dragon_attack(board.grid,Din) == 1:
                cases.lives -=1
            dragonshootdelay = time.time()
    
    #Obeying boundary constraints and simulating magnets present along the way
    cases.boundaryconstraints(board.grid,c,Din)
    cases.magnet(board.grid,Din)
    cases.beamcollision(board.grid,Din)
    if cases.drogopowerup(board.grid,Din) == 1:
        setme = 1
    Din.checkpowerup(setme)

    paisa.coin_render(coinsdict,board.grid)

    #Printing the screen and then clearing it up to reprint for the next instance of the gameplay
    print(board.draw_background(c))
    print('\033[H')

