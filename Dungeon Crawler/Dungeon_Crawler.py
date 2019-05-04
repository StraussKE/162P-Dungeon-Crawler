# preconfigured modules
import random

# self defined modules
# import constant
import helpMenu
import dungeon


def main():
    random.seed()
    playing = True

    helper = helpMenu.helpMenu()

    helper.welcome()
    
    while playing == True:
        searching_floor = true
        this_dungeon = dungeon.dungeon()
        if (difficulty == TUTORIAL):
                createTutorial(dungeon, current_floor, player_x, player_y, bounds)
        # if the player has selected any other difficulty level the program will shunt over to the regular level generation function
        else:
            createDungeon(dungeon, current_floor, player_x, player_y, difficulty, bounds)