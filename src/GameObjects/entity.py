from typing import override
from .GameObject import GameObject
from .item import Item
from ..settings import map_height, map_width
import random


class Entity(GameObject):
    def __init__(self,entity_id,position,render_img, hp, atk, stamina):
        self.position = position
        super().__init__(self.position,render_img)
        self.id = entity_id
        self.hp = hp
        self.atk = atk
        self.stamina = stamina
        
        pass

    @override
    def update(self):
        if self.hp > 0:
            self.move()
        else:
            self.die()
        pass

    def move(self, area):
        if self.hp<=0:
            self.die()
            return
        
        if self.stamina > 0:
            choice = random.choice([1, 2])

            def move_in_direction(current, target, max_value):
                if current < target and current < max_value - 1:
                    return current + 1
                elif current > target and current > 0:
                    return current - 1
                return current

            if choice == 1:
                self.x = move_in_direction(self.x, random.choice([self.x + 1, self.x - 1]), map_width)
            elif choice == 2:
                self.y = move_in_direction(self.y, random.choice([self.y + 1, self.y - 1]), map_height)

            for obj in area:
                if isinstance(obj, Item):

                    self.x = move_in_direction(self.x, obj.x, map_width)
                    self.y = move_in_direction(self.y, obj.y, map_height)
                    
                    if self.x == obj.x and self.y == obj.y:
                        self.interact_with_item(obj)

                elif isinstance(obj, Entity):
                    self.x = move_in_direction(self.x, obj.x, map_width)
                    self.y = move_in_direction(self.y, obj.y, map_height)

                    if self.x == obj.x and self.y == obj.y and obj.id != self.id:
                        self.attack(obj)

            self.stamina -= 1

        else:
            self.stamina += 10
            self.hp -= 1

    def interact_with_item(self, item):
        if item.name == "heal":
            self.hp += 10
            self.stamina += 5
            item.use_item()
        elif item.name == "atk":
            self.atk += 10
            item.use_item()
        elif item.name == "stamina":
            self.stamina += 10
            item.use_item()
    
    def attack(self, enemy:'Entity'):
        if self.stamina > 0:
            if self.x == enemy.x and self.y == enemy.y:
                if self.stamina >= 0:
                    enemy.hp -= self.atk
                    self.stamina -= 2

    def __str__(self):
        base_str = super().__str__()
        return f"{self.render_img} ID:{self.id} pos:{base_str}, HP: {self.hp}, ATK: {self.atk}, STAMINA: {self.stamina}"
