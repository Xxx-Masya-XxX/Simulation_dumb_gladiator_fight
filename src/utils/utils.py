import random
from src.settings import *
def rand_x():
    return random.randrange(0,map_width-1)
def rand_y():
    return random.randrange(0,map_height-1)