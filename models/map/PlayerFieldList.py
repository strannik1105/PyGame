from dataclasses import Field

from models.players.interfaces import IPlayer


class PlayerField:

    def __init__(self, player: IPlayer, field: Field):
        self.__player = player
        self.__field = field


class PlayerFieldList:
    __list = list()

    @staticmethod
    def add(player, field):
        PlayerFieldList.__list.append([player, field])

    @staticmethod
    def get(self):
        return self.__list

    @staticmethod
    def get(player: IPlayer) -> Field:
        for i in PlayerFieldList.__list:
            if i[0] is player:
                return i[1]
        return None

    @staticmethod
    def set(player: IPlayer, field: Field):
        for i in PlayerFieldList.__list:
            if i[0] is player:
                i[1] = field

    @staticmethod
    def remove(player: IPlayer):
        PlayerFieldList.__list.remove(PlayerFieldList.get(player))
