# preconfigured modules
import random

# self defined modules
# import constant

from dungeon import dungeon
from player import player

def main():
    this_player = player()
    this_dungeon = dungeon(this_player)
    while this_player.playing:
        print(this_dungeon)
        this_dungeon.move_target()

main()