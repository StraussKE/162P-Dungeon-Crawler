# preconfigured modules
import random

# self defined modules
# import constant
import helpMenu
import dungeon


def main():
    playing = True

    helper = helpMenu.helpMenu()

    helper.welcome()
    
    while playing == True:
        searching_floor = true
        this_dungeon = dungeon()