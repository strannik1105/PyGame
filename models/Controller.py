from models.map.PlayerFieldList import PlayerFieldList
from models.map.map import Map
from models.players.Player import Player
from models.players.PlayerDamageable import PlayerDamageable
from models.players.PlayerAttacker import PlayerAttacker


class Controller:

    def __init__(self):
        print('Map: ')
        print('Input n: ', end='')
        n = int(input())
        print('Input m: ', end='')
        m = int(input())
        self.__map = Map(n, m)
        print('PlayerA: ')
        print('Render: ', end='')
        render = input()
        print('Health: ', end='')
        health = int(input())
        print('Attack: ', end='')
        attack = int(input())
        self.__playerA = PlayerAttacker(render, health, attack)
        self.__map.AddPlayer(self.__playerA)
        print('PlayerB: ')
        print('Render: ', end='')
        render = input()
        print('Health: ', end='')
        health = int(input())
        print('Attack: ', end='')
        attack = int(input())
        self.__playerB = PlayerAttacker(render, health, attack)
        self.__map.AddPlayer(self.__playerB)
        print('PlayerC: ')
        print('Render: ', end='')
        render = input()
        self.__playerC = Player(render)
        self.__map.AddPlayer(self.__playerC)
        self.__turn = 0

    def Play(self):
        self.__map.PrintMap()
        while True:
            if self.__turn == 0:
                self.PlayerAMove()
            elif self.__turn == 1:
                self.PlayerBMove()
            elif self.__turn == 2:
                self.PlayerCMove()
            self.__map.PrintMap()

    def PlayerAMove(self):
        print('PlayerA turn')
        print('Your position: ', end='')
        old_x = PlayerFieldList.get(self.__playerA).x
        print(old_x, end=' ')
        old_y = PlayerFieldList.get(self.__playerA).y
        print(old_y)
        while True:
            print('Input x change(ex: 1; 0; -1): ', end=' ')
            x = int(input())
            print('Input y change(ex: 1; 0; -1): ', end=' ')
            y = int(input())
            if((abs(x) == 1) and (abs(y) <= 1)) or ((abs(x) <= 1) and (abs(y) == 1)):
                if self.__map.Move(self.__playerA, old_x + x, old_y + y):
                    break
                else:
                    from models.map.fieldMovable import FieldMovable
                    if isinstance(self.__map.GetField(old_x + x, old_y + y), FieldMovable):
                        if isinstance(self.__map.GetField(old_x + x, old_y + y).GetPlayer(), PlayerDamageable):
                            self.__playerA.AttackVictim(self.__map.GetField(old_x + x, old_y + y).GetPlayer())
                            break
                    print('Incorrect turn')
            else:
                print('Incorrect turn')
        print()
        self.__turn = 1

    def PlayerBMove(self):
        print('PlayerB turn')
        print('Your position: ', end='')
        old_x = PlayerFieldList.get(self.__playerB).x
        print(old_x, end=' ')
        old_y = PlayerFieldList.get(self.__playerB).y
        print(old_y)
        while True:
            print('Input x change(ex: 1; 0; -1): ', end=' ')
            x = int(input())
            print('Input y change(ex: 1; 0; -1): ', end=' ')
            y = int(input())
            if((abs(x) == 1) and (abs(y) <= 1)) or ((abs(x) <= 1) and (abs(y) == 1)):
                if self.__map.Move(self.__playerB, old_x + x, old_y + y):
                    break
                else:
                    from models.map.fieldMovable import FieldMovable
                    if isinstance(self.__map.GetField(old_x + x, old_y + y), FieldMovable):
                        if ((abs(x) == 1) and (abs(y) == 0)) or ((abs(x) == 0) and (abs(y) == 1)):
                            if(isinstance(self.__map.GetField(old_x + x, old_y + y).GetPlayer(), PlayerDamageable)):
                                self.__playerB.AttackVictim(self.__map.GetField(old_x + x, old_y + y).GetPlayer())
                                break
                    print('Incorrect turn')
            else:
                print('Incorrect turn')
        print()
        self.__turn = 2

    def PlayerCMove(self):
        print('PlayerC turn')
        print('Your position: ', end='')
        old_x = PlayerFieldList.get(self.__playerC).x
        print(old_x, end=' ')
        old_y = PlayerFieldList.get(self.__playerC).y
        print(old_y)
        while True:
            print('Input x change(ex: 1; 0; -1): ', end=' ')
            x = int(input())
            print('Input y change(ex: 1; 0; -1): ', end=' ')
            y = int(input())
            if ((abs(x) == 1) and (abs(y) <= 1)) or ((abs(x) <= 1) and (abs(y) == 1)):
                if self.__map.Move(self.__playerC, old_x + x, old_y + y):
                    break
                else:
                    print('Incorrect turn')
            else:
                print('Incorrect turn')
        print()
        self.__turn = 0
