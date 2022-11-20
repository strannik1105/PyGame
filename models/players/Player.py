from models.players.interfaces.IPlayer import IPlayer


class Player(IPlayer):

    def __init__(self, render: str, health=100, attack=20):
        self.__health = health
        self.__attack = attack
        self.__render = render

    @property
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value):
        self.__health = value

    @property
    def Attack(self):
        return self.__attack

    @Attack.setter
    def Attack(self, value):
        self.__attack = value

    @property
    def Render(self):
        return self.__render

    @Render.setter
    def Render(self, value):
        self.__render = value
