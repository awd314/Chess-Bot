import pygame as pg
from settings import SQUARE_SIZE

piecesDictionary = {
    -1 : None,
    0 : pg.transform.scale(pg.image.load("./images/wpawn.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    1 : pg.transform.scale(pg.image.load("./images/bpawn.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    2 : pg.transform.scale(pg.image.load("./images/wbishop.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    3 : pg.transform.scale(pg.image.load("./images/bbishop.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    4 : pg.transform.scale(pg.image.load("./images/wknight.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    5 : pg.transform.scale(pg.image.load("./images/bknight.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    6 : pg.transform.scale(pg.image.load("./images/wrook.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    7 : pg.transform.scale(pg.image.load("./images/brook.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    8 : pg.transform.scale(pg.image.load("./images/wqueen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    9 : pg.transform.scale(pg.image.load("./images/bqueen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    10 : pg.transform.scale(pg.image.load("./images/wking.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    11 : pg.transform.scale(pg.image.load("./images/bking.png"), (SQUARE_SIZE, SQUARE_SIZE)),
}