from colorama import Fore,Back

MAX_Y = 1055
MAX_X = 40
LIVES = 6
Coin = Fore.YELLOW + '$' + '\x1b[0m'
Bullet = Fore.LIGHTYELLOW_EX + 'o' + '\x1b[0m' 
Obstacle = Back.LIGHTYELLOW_EX + '|' + '\x1b[0m'
Iceball = Back.CYAN + 'O' + '\x1b[0m'
Powerup = Back.MAGENTA + "P" + '\x1b[0m'
DragonPowerUp = Back.LIGHTWHITE_EX + 'D' + '\x1b[0m'
Magnet = Back.RED + 'M' + '\x1b[0m'