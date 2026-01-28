from interface import *
from board import *

if __name__ == "__main__":
    brd = Board([
        [8, 4, 6, 10, 12, 6, 4, 8],
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [7, 3, 5, 9, 11, 5, 3, 7]
    ], 0, -1, False, False)

    def test_func(inter):
        pass

    inter = Interface("test interface", brd, test_func)

    inter.loop()

    pg.quit()