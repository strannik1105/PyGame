import abc

from models.players.interfaces.IPlayer import IPlayer


class Field(abc.ABC):

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


    @abc.abstractmethod
    def Render(self):
        pass

    @abc.abstractmethod
    def MoveIn(self):
        pass

    @abc.abstractmethod
    def RemovePlayer(self):
        pass

    @abc.abstractmethod
    def GetPlayer(self):
        pass