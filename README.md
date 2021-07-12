# Shellpack Joyride on Terminal  
Shellpack Joyride is a terminal-based Python game, inspired from *Jetpack Joyride*.  
![Gameplay.png](https://github.com/bhattsahil1/ShellpackJoyride/blob/master/gameplay.png?raw=true)  

    
# Instructions

* Launch the game 
```
python3 main.py
```

* Objective of the game is to defeat the enemy within the given time(40 seconds) and within the limited number of lives(6).

# Controls

* Use w,a,d for Movement.(w - moving up, a - moving left, d - moving right )
* Use s to shoot bullets at obstacles and the enemy.
* Use spacebar to activate shield around the player.Note that this will last for just 10 seconds, and can be used again only after a gap of 40 seconds after use.
* Use q to quit the game.

# Features

* The game involves OOPS concepts (Abstraction,Inheritance,Polymorphism and Encapsulation).
* The game consists of several obstacles in the form of firebeams and magnets, which need to be overcome.
* Powerups to speed up the game and also to change from normal player mode to Dragon-mode have been included.
* The enemy dragon replicates the movement of the player along the y-axis,while constantly firing ice-balls at it. 

# Scoring and Objectives

* Keep collecting coins along the way
* Destroy firebeams, collect powerups.
* Win the game by killing the enemy dragon using bullets
* Wait for the final message from none other than Master Yoda.  

# Requirements

* Python3
* Colorama
* Pygame (*Only for background music*)
