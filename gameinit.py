import os
from surroundings import Surroundings
from background import Board

class GameInit:

    def gamestart(Board):
        surr = Surroundings()
        surr.create_ground(Board)
        surr.create_sky(board.grid)
        surr.create_coins(board.grid)
        surr.create_clouds(board.grid,2,11)
        surr.create_firebeam(board.grid)
        surr.create_powerups(board.grid)
        surr.create_viserion(board.grid)