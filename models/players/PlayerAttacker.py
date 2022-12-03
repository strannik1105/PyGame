from models.players.PlayerDamageable import PlayerDamageable


class PlayerAttacker(PlayerDamageable):
    def __init__(self, render: str, health=100, attack=20):
        self.__attack = attack
        super(PlayerAttacker, self).__init__(render, health)

    @property
    def Attack(self):
        return self.__attack

    @Attack.setter
    def Attack(self, value):
        self.__attack = value

    def AttackVictim(self, victim: PlayerDamageable):
        #victim.Health = victim.Health - self.Attack
        victim.Damage(self.Attack)
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
