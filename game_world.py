from entity import Entity
from item import Item
from settings import *
from collections import Counter

class GameWorld:
    def __init__(self, objects):
        self.objects = objects
        self.game_status = True
        pass
    def get_objects(self):
        return self.objects
    def update(self):
        type_counts = Counter(type(obj) for obj in self.objects)
        if self.game_status:
            if type_counts.get(Entity, 0) >1:
                for g_obj in self.objects:
                    if type(g_obj) is Item:
                        if g_obj.is_used():
                            self.objects.pop(self.objects.index(g_obj))
                    if type(g_obj) is Entity:
                        if g_obj.is_dead() == False:
                            poss = g_obj.get_poss_around()
                            area = [i for i in self.objects if i.get_pos() in poss ]
                            g_obj.move(area)
                        else:
                            self.objects.pop(self.objects.index(g_obj))
                
                
            else:
                # os.system('cls' if os.name == 'nt' else 'clear')
                self.game_status = False
                # print("Симуляция закончилась")
                pass