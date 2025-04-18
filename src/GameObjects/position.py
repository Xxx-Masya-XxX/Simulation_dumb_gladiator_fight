class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

    def get_poss_around(self):
        return [
            (self.x+1,self.y),
            (self.x-1,self.y),
            (self.x,self.y+1),
            (self.x,self.y-1),
            (self.x,self.y),
        ]

    def __str__(self):
        return f"pos{self.x,self.y}"