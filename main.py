from models.map.PlayerFieldList import PlayerFieldList
from models.map.map import Map
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from models.players.Player import Player
from models.players.PlayerAttacker import PlayerAttacker


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    map = Map(10, 5)
    player1 = PlayerAttacker('1', attack=110)
    player2 = Player('2')
    map.AddPlayer(player1)
    map.AddPlayer(player2)
    while True:
        map.PrintMap()
        field = PlayerFieldList.get(player1)
        print(field.x, end=' ')
        print(field.y)
        x = int(input())
        y = int(input())
        map.Move(player1, x, y)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
