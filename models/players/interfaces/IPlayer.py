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

    @property
    @abc.abstractmethod
    def Render(self):
        pass

    @Render.setter
    @abc.abstractmethod
    def Render(self, value):
        pass