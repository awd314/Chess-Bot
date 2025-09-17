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
        i, j = 0, 0
        while self.inter.running:
            self.inter.clock.tick(60)
            j += 0.1
            if j >= 8:
                j = 0
                i += 1
                if i ==8:
                    i = 0
            self.inter.CheckEvents()

            self.inter.screen.fill("#000000")
            self.inter.DrawBoard(self.board.miniBoard, self.board.flipped)
            self.inter.TestFunction(self.board.GetWhiteQueenMoves((int(i), int(j)), self.board.miniBoard))

            pg.display.flip()


if __name__ == "__main__":
    m = Main()
    m.Loop()
    pg.quit()