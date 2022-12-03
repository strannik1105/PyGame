from models.players.Player import Player


class PlayerDamageable(Player):

    def __init__(self, render: str, health=100):
        self.__health = health
        super(PlayerDamageable, self).__init__(render)

    @property
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value):
       self.__health = value

    def Damage(self, value: int):
        self.__health = self.Health - value