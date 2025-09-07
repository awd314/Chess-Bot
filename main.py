from interface import *
from board import *


class Main:
    def __init__(self):
        self.inter = Interface()
        self.board = Board()
    

    def Loop(self):
        while self.inter.running:
            self.inter.CheckEvents()

            self.inter.screen.fill("#000000")
            self.inter.DrawBoard(self.board.miniBoard, self.board.flipped)

            pg.display.flip()


if __name__ == "__main__":
    m = Main()
    m.Loop()
    pg.quit()