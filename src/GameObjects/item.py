from .GameObject import GameObject


class Item(GameObject):
    def __init__(self,position,render_img, name,params:dict):
        super().__init__(position,render_img)
        self.name = name
        self.params = params
        self.is_used_flag = False
        self.count_use = 1

    def is_used(self):
        return self.is_used_flag

    def use_item(self):
        self.is_used_flag =True
        return self.params