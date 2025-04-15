from .GameObjects.entity import Entity
from .GameObjects.item import Item
from .settings import *
from collections import Counter

class GameWorld:
    def __init__(self, objects):
        self.objects = objects
        self.game_status = True
        pass
    def get_objects(self):
        return self.objects
