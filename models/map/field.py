import abc

from models.players.interfaces.IPlayer import IPlayer


class Field(abc.ABC):

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @abc.abstractmethod
    def Render(self):
        pass

    @abc.abstractmethod
    def MoveIn(self):
        pass
