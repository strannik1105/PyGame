from models.players.interfaces.IPlayer import IPlayer


class Player(IPlayer):


    def __init__(self, health=0, attack=0):
        self.__health = health
        self.__attack = attack

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

    def AttackPlayer(self, player):
        player.Health = player.Health - self.__attack