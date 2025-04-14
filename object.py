from position import Position

class GameObject(Position):
    def __init__(self,position:Position,render_img:str):
        super().__init__(position.x,position.y)
        self.render_img = render_img
        pass
    def __str__(self):
        return f"{self.get_pos()}"
        pass
    def set_img(self,new_img):
        self.render_img = new_img
    def update(self):
        pass