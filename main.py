from models.map.PlayerFieldList import PlayerFieldList
from models.PlayersActions import PlayersActions
from models.map.map import Map
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from models.players.Player import Player


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    map = Map(10, 5)
    player1 = Player('1')
    map.AddPlayer(player1)
    map.PrintMap()
    field = PlayerFieldList.get(player1)
    map.Move(player1, field.x + 1, field.y)
    map.PrintMap()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
