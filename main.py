from models.Controller import Controller
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
    game = Controller()
    game.Play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
