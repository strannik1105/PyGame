from models.players.interfaces.IPlayer import IPlayer
from models.map.field import Field


class FieldInvaded(Field):

    def __init(self, x: int, y: int, player=None):
        super().__init__(x, y)
        self.__player = player

    def MoveIn(self, player):
        print("You can't do this")

    def RemovePlayer(self):
        self.__player = None

    def Render(self):
        return 'x'
