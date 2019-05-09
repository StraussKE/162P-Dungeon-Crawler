# preconfigured modules
import random

# self defined modules
# import constant
import helpMenu
from dungeon import dungeon


def main():
    playing = True

    helper = helpMenu.helpMenu()

    helper.welcome()
    
    while playing == True:
        searching_floor = True
        this_dungeon = dungeon()
        print(this_dungeon)
        playing = False

main()