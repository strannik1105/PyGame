import abc


class IPlayer(abc.ABC):

#    @abc.abstractmethod
#    def __init(self, health):
#        self.__health = health

    @property
    @abc.abstractmethod
    def Health(self):
        pass

    @Health.setter
    @abc.abstractmethod
    def Health(self, value):
        pass


    @property
    @abc.abstractmethod
    def Attack(self):
        pass


    @Health.setter
    @abc.abstractmethod
    def Attack(self, value):
        pass