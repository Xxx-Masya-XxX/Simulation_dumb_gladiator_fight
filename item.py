from object import GameObject


class Item(GameObject):
    def __init__(self,position,render_img, name,):
        super().__init__(position,render_img)
        self.name = name
        # self.hp = hp
        # self.atk = atk
        # self.stamina = stamina
        self.is_used_flag = False
        pass
    def is_used(self):
        return self.is_used_flag
    def use_item(self):
        self.is_used_flag =True