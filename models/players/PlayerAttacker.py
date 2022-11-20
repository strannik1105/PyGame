from models.players.Player import Player
from models.players.interfaces.IPlayer import IPlayer


class PlayerAttacker(Player):
    def __init__(self, render: str, health=100, attack=20):
        super(PlayerAttacker, self).__init__(render, health, attack)

    def AttackVictim(self, victim: IPlayer):
        victim.Health = victim.Health - self.Attack
        print(self.Render, end='(')
        print(self.Attack, end=') ')
        print('attack', end=' ')
        print(victim.Render, end='(')
        print(victim.Health, end=')')
        print('')

        if victim.Health <= 0:
            print(victim.Render, end=' ')
            print('lose')
            exit()
