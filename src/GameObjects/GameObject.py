from .position import Position

class GameObject(Position):
    def __init__(self,position:Position,render_img:str):
        super().__init__(position.x,position.y)
        self.render_img = render_img
        self.__is_alive = True
    
    def update(self):
        pass

    def start(self):
        pass

    def __str__(self):
        return f"{self.get_pos()}"

    def set_img(self,new_img):
        self.render_img = new_img
    
    def die(self):
        self.__is_alive = False
        
    def is_alive(self):
        return self.__is_alive