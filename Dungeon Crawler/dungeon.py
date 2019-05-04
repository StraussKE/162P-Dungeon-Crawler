# standard modules
import random

#user created modules
import constant
import validation

class dungeon(object):
    """the dungeon being explored"""

    def __init__(self):
        self.current_difficulty = self._set_difficulty()
        self.bounds = self._set_bounds(self.current_difficulty)
        self.dungeon = [] # dungeon will be best as a list of floors, floors are a list of coordinate tuples
        self.current_floor = 0

        self._create_dungeon(self.bounds)
        self.stringify_dung = ''

    def __str__(self):
        self.stringify_dung += constant.STARBAR + "\n"
        self.stringify_dung += "You are on level " + str(self.current_floor + 1) + " of the dungeon.\n"
        self.stringify_dung += constant.STARBAR + "\n"

        self.stringify_dung += str(self.dungeon[self.current_floor]) + "\n"

        self.stringify += ("\nKey:    " + constant.PLAYER + " = Hero    " + constant.TRAP 
                           + " = Trap    " + constant.TREASURE + " = Treasure    "
                           + constant.SMALL_BOULDER + " = Small Rock\n" + constant.STAIRS_DOWN 
                           + " = Stairs Down    " + constant.STAIRS_UP + " = Stairs Up\n\n")
        return self.stringify_dung

    def _set_difficulty(self):
        print("\nPlease select your difficulty level. If you've never played before the tutorial\n"
            + "is highly recommended for explaining basic commands and mechanics. If you ever \n"
            + "need to review anything while exploring, just access our help menu by pressing H\n"
            + "\t" + str(constant.TUTORIAL) + ": Tutorial\n"
            + "\t" + str(constant.EASY) + ": Easy\n"
            + "\t" + str(constant.NORMAL) + ": Normal\n"
            + "\t" + str(constant.HARD) + ": Hard\n")
        return validation.intInput(1,4)

    def _set_bounds(self, difficulty):
        if(difficulty == constant.TUTORIAL):
            return constant.TUTORIAL_DIMENSION
        if(difficulty == constant.EASY):
            return constant.EASY_DIMENSION
        if(difficulty == constant.NORMAL):
            return constant.NORMAL_DIMENSION_MAX
        if(difficulty == constant.HARD):
            return constant.HARD_DIMENSION_MAX

    #creates dungeon
    def _create_dungeon(self, bounds):
        floor_num = 0
        while floor_num < bounds:
            self.dungeon.append(self.dungeon_floor(bounds, floor_num))
            floor_num += 1

    # generates empty spaces
    class dungeon_floor(object):
        def __init__(self, bounds, floor_number):
            self.bounds = bounds
            self.this_floor = []
            self.stairs_down = 1
            self.treasure = 1
            self.key = 1
            self.traps = 1
            self.small_rock = 1
            self.boulder = 1
            self.portal = 1

            self._create_floor(self.bounds)
            self._stringify_floor =''

        def _draw_row(self, symbol):
            self.row = '|'
            if (row_num == -1):
                self.row.iter = 0
                while self.row_iter < self.bounds:
                    self.row += symbol
                    self.row_iter += 1
            return self.row

        def __str__(self):
            # generate the perimeter lines
            self.perimeter = _draw_row(constant.PERIMETER_LINE)
            #generate the lines depicting space between rows
            self.grid_row = _draw_row(constant.GRID_SQUARE_LINE)

            self.stringify_floor += perimeter
            self.strinfigy_floor += "\n"
            for row in iter(current_floor):
                self.strinfify_floor += ("|" + self.current_floor[row] + "|")
                self.stringify_floor += "\n"
                if(row == current_floor.length):
                    self.stringify_floor += self.perimeter
                else:
                    self.stringify_floor += self.grid_row
                    self.stringify_floor += "\n"
            return self.stringify_floor

        # Populates the dungeon floor with empty dungeon spaces
        def _create_floor(self, bounds):
            row_num = 0
            while row_num < bounds:
                self.this_floor.append(self._generate_empty_row(bounds))
                row_num += 1

        def _generate_empty_row(self, bounds):
            square_num = 0
            this_row = []
            while square_num < bounds:
                this_row.append(constant.EMPTY)
                square_num += 1
            return this_row


class tutorial(dungeon):
    # Specific dungeon experience for players wishing to go through the tutorial
    def __init__(self):
        self.stairs_down = 1
        self.treasure = 1
        self.key = 1
        self.traps = 1
        self.small_rock = 1
        self.boulder = 1
        self.portal = 1
    

        

    def insert_player(self)
    self.dungeon

    if (current_floor < bounds - 1)
    {
        placeObject(dungeon, current_floor, bounds, stairs_down, STAIRS_DOWN);
        // we have stairs to descend further into the dungeon unless we are on the final floor
    }

    if (current_floor == 0)
    {
        std::cin.ignore();
        aboutMovement();
        aboutStairs();
        std::cout + "\nWhy don't you try getting to the stairs on this floor?\n\n";
    }

    if (current_floor == 1)
    {
        placeObject(dungeon, current_floor, bounds, treasure, TREASURE);
        // we have placed our treasure

        placeObject(dungeon, current_floor, bounds, key, KEY);
        // we have placed our key

        std::cin.ignore();
        aboutTreasure();

        std::cout + "\nWhy don't you try getting the treasure from this floor?\n\n";

    }
    if (current_floor == 2)
    {
        placeObject(dungeon, current_floor, bounds, traps, TRAP);
        // we have placed our traps

        placeObject(dungeon, current_floor, (bounds - 1), small_rock, SMALL_BOULDER);
        // we have small rocks

        placeObject(dungeon, current_floor, bounds, boulder, LARGE_BOULDER);
        // we have boulders

        std::cin.ignore();
        aboutTraps();
        aboutBoulders();

        std::cout + "\nWhy don't you try disarming the trap on this floor?\n\n";
    }
    if (current_floor == (bounds - 1))
    {
        placeObject(dungeon, current_floor, bounds, portal, PORTAL);
        // we have our portal

        std::cin.ignore();
        aboutPortals();

        std::cout + "\nHead through the portal to finish this tutorial.\n\n";