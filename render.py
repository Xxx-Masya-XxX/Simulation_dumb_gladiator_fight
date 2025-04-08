from settings import *
from entity import Entity
from item import Item
from collections import Counter
import os


class Render:
    def __init__(self, game_world: list):
        self.world = game_world
        self.render_frame = 1

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        # Генерация 2D массива карты
        matrix = [["." for _ in range(map_width)] for _ in range(map_height)]

        # Ставим объекты на карту
        for obj in self.world.get_objects():
            pos = obj.get_pos()
            matrix[pos[1]][pos[0]] = obj.render_img

        # Счётчики
        type_counts = Counter(type(obj) for obj in self.world.get_objects())
        print("tick:", self.render_frame,
              "entities:", type_counts.get(Entity, 0),
              "items:", type_counts.get(Item, 0))
        self.render_frame += 1

        # Получаем список сущностей (Entity)
        entities = [obj for obj in self.world.get_objects() if isinstance(obj, Entity)]

        # Определяем ширину карты (в символах)
        map_width_in_chars = map_width * 2  # т.к. после каждой ячейки пробел

        # Печатаем карту и состояния объектов рядом
        for y, row in enumerate(matrix):
            row_str = " ".join(row)
            print(row_str.ljust(map_width_in_chars), end="")

            # Если есть Entity для этой строки — выводим
            if y < len(entities):
                print(" | ", entities[y])
            else:
                print()

        print()  # пустая строка после карты
