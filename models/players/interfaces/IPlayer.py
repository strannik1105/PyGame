import abc


class IPlayer(abc.ABC):

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

    @abc.abstractmethod
    def AttackPlayer(self, player):
        pass