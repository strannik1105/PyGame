import random

from models.map.field import Field
from models.map.fieldMovable import FieldMovable
from models.players.interfaces import IPlayer


class Map:
    # n x m map
    def __init__(self, n: int, m: int):
        self.__n = n
        self.__m = m
        map = list()
        for i in range(0, n):
            sublist = list()
            for j in range(0, m):
                sublist.append(FieldMovable(i, j))
            map.append(sublist)
        self.__map = map

    def AddPlayer(self, player: IPlayer):
        while True:
            x = random.randint(0, self.__n - 1)
            y = random.randint(0, self.__m - 1)
            if self.__map[x][y].MoveIn(player):
                break

    def PrintMap(self):
        for i in range(0, self.__n):
            for j in range(0, self.__m):
                print(self.__map[i][j].Render(), end=' ')
            print('')