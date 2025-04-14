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

class Game:
    game_status = True
    def start(self):
        self.game_objs_list = [
            Entity(position=Position(rand_x(),rand_y()),entity_id=1,render_img="😎",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=2,render_img="🧑🏻",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=3,render_img="👴",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=4,render_img="🥺",hp=10,atk=1,stamina=100),
            Entity(position=Position(rand_x(),rand_y()),entity_id=5,render_img="👨🏿",hp=10,atk=1,stamina=100),
        ]
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="🩹",name="heal")
            for _ in range(random.randint(10, 40))
            ]
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="🪓",name="atk")
            for _ in range(random.randint(10, 40))
            ]
        self.game_objs_list +=[ 
            Item(position=Position(rand_x(),rand_y()),render_img="⚡",name="stamina")
            for _ in range(random.randint(10, 40))
            ]
        self.game_world = GameWorld(objects=self.game_objs_list)
        
        # рендер в окне
        app = QApplication(sys.argv)
        self.rend = GameWindow(game_world=self.game_world)
        self.rend.show()
        sys.exit(app.exec())
        # рендер в консоли
        # self.rend = Render(game_world=self.game_world)
            
    def update(self):
        type_counts = Counter(type(obj) for obj in self.game_objs_list)
        if type_counts.get(Entity, 0) >0:
            for g_obj in self.game_objs_list:
                if type(g_obj) is Item:
                    if g_obj.is_used():
                        self.game_objs_list.pop(self.game_objs_list.index(g_obj))
                if type(g_obj) is Entity:
                    if g_obj.is_dead() == False:
                        poss = g_obj.get_poss_around()
                        area = [i for i in self.game_objs_list if i.get_pos() in poss ]
                        g_obj.move(area)
                    else:
                        self.game_objs_list.pop(self.game_objs_list.index(g_obj))
            
            self.rend.render()
        else:
            # os.system('cls' if os.name == 'nt' else 'clear')
            self.game_status = False
            # print("Симуляция закончилась")
            pass
            

if __name__ == "__main__":
    game = Game()
    game.start()
    while game.game_status == True:
        game.update()
        time.sleep(.1)
        # break
        pass
    pass