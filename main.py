### NOTE Uncomment board line on 'self.flipped' variable to get a random color at the beginning of the game


from interface import *
from board import *


class Main:
    """
    Main class of the project, calls the interface, a board and the bot
    to blend everything together.
    """
    def __init__(self):
        self.inter = Interface()
        self.board = Board()
    

    def Loop(self):
        """
        Runs the game with key listener, board drawing and bot decision.
        """
        while self.inter.running:
            self.inter.clock.tick(60)
            self.inter.CheckEvents()

            self.inter.screen.fill("#000000")
            self.inter.DrawBoard(self.board.miniBoard, self.board.flipped)
            #self.inter.TestFunction(self.board.GetWhiteKnightMoves((7, 1)))

            pg.display.flip()


if __name__ == "__main__":
    m = Main()
    m.Loop()
    pg.quit()