from src.Renders.render_window import GameWindow
from src.Game import Game
  

if __name__ == "__main__":
    game = Game(GameWindow)
    game.start()
    # while game.game_status == True:
    #     game.update()
    #     time.sleep(.1)
    #     # break
    #     pass
    pass