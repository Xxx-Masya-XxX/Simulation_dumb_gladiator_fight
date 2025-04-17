from .game_world import GameWorld
from .GameObjects.entity import Entity
from .GameObjects.item import Item
from .settings import *
from .GameObjects.position import Position
import random
from collections import Counter
from PySide6.QtWidgets import QApplication
import sys
from .utils.utils import rand_x, rand_y


class Game:
    game_status = True
    game_tick = 1
    def __init__(self,render_class):
        self.render_class = render_class
        
    def start(self):
        self.game_objs_list = [
            Entity(position=Position(rand_x(),rand_y()),entity_id=1,render_img="😎",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=2,render_img="🧑🏻",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=3,render_img="👴",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=4,render_img="🥺",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=5,render_img="👨🏿",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=6,render_img="🧙‍♂️",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=7,render_img="🤖",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=8,render_img="🎩",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=9,render_img="🥵",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=10,render_img="🤑",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=11,render_img="🕵️‍♂️",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=12,render_img="🧐",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=13,render_img="🦸‍♂️",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=14,render_img="👹",hp=10,atk=1,stamina=100),
        ]
        
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="🩹",name="heal",params={
                'hp':10,
                'stamina':3, 
            })
            for _ in range(random.randint(10, 40))
            ]
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="🪓",name="atk",params={
                'atk':10,    
            })
            for _ in range(random.randint(10, 40))
            ]
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="🍯",name="atk",params={
                'atk':40,
                'hp':40,
                'duration':30   
            })
            for _ in range(random.randint(10, 40))
            ]
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="🪤",name="poison",params={
                'hp':-10,   
            })
            for _ in range(random.randint(10, 40))
            ]
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="⚡",name="stamina",params={
                'stamina':10,    
            })
            for _ in range(random.randint(10, 40))
            ]
        self.game_world = GameWorld(objects=self.game_objs_list)
        # 🪤
        # 💣🧨🔫💊
        # 
        # 
        # 
        # 
        # 
        # 
        # рендер в окне
        app = QApplication(sys.argv)
        self.rend = self.render_class(game=self)
        self.rend.show()
        sys.exit(app.exec())

        # рендер в консоли нужно бы пофиксить но мне похуй
        # self.rend = self.render_class(game_world=self.game_world)
        
        # рендер в pygame
        # self.rend = self.render_class()
        # self.rend.run(self)
            
    def update(self):
        type_counts = Counter(type(obj) for obj in self.game_objs_list)
        if type_counts.get(Entity, 0) >1:
            
            for g_obj in self.game_objs_list:
                if type(g_obj) is Item:
                    if g_obj.is_used():
                        self.game_objs_list.pop(self.game_objs_list.index(g_obj))
                if type(g_obj) is Entity:
                    if g_obj.is_alive():
                        poss = g_obj.get_poss_around()
                        area = [i for i in self.game_objs_list if i.get_pos() in poss ]
                        g_obj.move(area)
                    else:
                        self.game_objs_list.pop(self.game_objs_list.index(g_obj))
        else:
            # os.system('cls' if os.name == 'nt' else 'clear')
            self.game_status = False
            # print("Симуляция закончилась")
            pass
        self.game_tick +=1
        
    def is_over(self):
        return self.game_status