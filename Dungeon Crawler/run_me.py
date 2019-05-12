# preconfigured modules
import random

# self defined modules
# import constant
import validation
from dungeon import dungeon
from player import player

def main():
    this_player = player()
    this_dungeon = dungeon(this_player)
    while this_player.playing:
        print(this_dungeon)
        this_dungeon.move_target()
        if this_dungeon.finished:
            print("Congratulations, you have successfully completed this dungeon.\n" +
                  "Final inventory is:\n" + this_player.str_inventory +
                  "\nWould you like to select a new difficulty and continue your adventure?\n")
            if validation.yes_or_no():
                this_dungeon = dungeon(this_player)
            else:
                this_player.playing = False
main()