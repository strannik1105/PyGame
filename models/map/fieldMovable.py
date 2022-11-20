import models.players.Player
from models.map.PlayerFieldList import PlayerFieldList
from models.map.field import Field
from models.players.Player import Player
from models.players.interfaces.IPlayer import IPlayer


class FieldMovable(Field):

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.__player = None

    def __init(self, x: int, y: int, player: IPlayer = None):
        super().__init__(x, y)
        self.__player = player

    def MoveIn(self, player: IPlayer):
        if self.__player is None:
            self.__player = player
            return True
        return False

    def RemovePlayer(self):
        if self.__player is not None:
            #PlayerFieldList.remove(self.__player)
            self.__player = None

    def Render(self):
        if self.__player is not None:
            return self.__player.Render
        return '0'

    def GetPlayer(self):
        return self.__player