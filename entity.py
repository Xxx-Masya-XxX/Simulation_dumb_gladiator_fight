from object import GameObject
from item import Item
from settings import map_height, map_width
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
    def is_dead(self):
        if self.hp >0:
            return False
        else: return True
    def move(self, area):
        if self.stamina >0:
            choice = random.randrange(0, 3)
            
            if choice == 1:
                if self.x < map_width - 1:
                    self.x += 1
                else:
                    self.x -= 1
            elif choice == 2:
                if self.y < map_height - 1:
                    self.y += 1
                else:
                    self.y -= 1

            for i in area:
                if isinstance(i, Item):
                    # Движение к предмету
                    if self.x < i.x and self.x < map_width - 1:
                        self.x += 1
                    elif self.x > i.x and self.x > 0:
                        self.x -= 1
                    elif self.y < i.y and self.y < map_height - 1:
                        self.y += 1
                    elif self.y > i.y and self.y > 0:
                        self.y -= 1

                    # Взаимодействие
                    if self.x == i.x and self.y == i.y:
                        if i.name == "heal":
                            self.hp += 4
                            i.use_item()

                elif isinstance(i, Entity):
                    # Движение к другому существу
                    if self.x < i.x and self.x < map_width - 1:
                        self.x += 1
                    elif self.x > i.x and self.x > 0:
                        self.x -= 1
                    elif self.y < i.y and self.y < map_height - 1:
                        self.y += 1
                    elif self.y > i.y and self.y > 0:
                        self.y -= 1

                    # Атака
                    if self.x == i.x and self.y == i.y:
                        self.attack(i)

            self.stamina -= 1
        else: 
            self.hp-=1

    
    def attack(self,enemy):
        if self.hp >0:
            if self.stamina >0 and self.hp >3:
                if self.stamina -self.atk >=0:
                    enemy.hp-=self.atk
                    self.stamina -= 2
        else:
            del self
        pass
    
    def use_item(self):
        pass
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, HP: {self.hp}, ATK: {self.atk}, STAMINA: {self.stamina}"
