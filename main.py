from render import Render
from render_window import GameWindow
from game_world import GameWorld
from entity import Entity
from item import Item
from settings import *
import time
from position import Position
import random
import os
from collections import Counter
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QLabel,QListWidget,QVBoxLayout,QHBoxLayout
import sys
from utils import rand_x, rand_y
from Game import Game
  

if __name__ == "__main__":
    game = Game(GameWindow)
    game.start()
    # while game.game_status == True:
    #     game.update()
    #     time.sleep(.1)
    #     # break
    #     pass
    pass