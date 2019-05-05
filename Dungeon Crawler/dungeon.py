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

    def __str__(self):
        stringify_dung = constant.STARBAR
        stringify_dung += ("You are on level " + str(self.current_floor + 1) + " of the dungeon.\n")
        stringify_dung += (constant.STARBAR + "\n")

        stringify_dung += str(self.dungeon[self.current_floor])

        stringify_dung += ("\n\nKey:    " + constant.PLAYER + " = Hero    " + constant.TRAP 
                           + " = Trap    " + constant.TREASURE + " = Treasure    "
                           + constant.SMALL_BOULDER + " = Small Rock\n" + constant.STAIRS_DOWN 
                           + " = Stairs Down    " + constant.STAIRS_UP + " = Stairs Up\n\n")
        return stringify_dung

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

            self._create_floor()

        def _draw_row(self, symbol):
            row = '|'
            col_num = 0
            while col_num < self.bounds:
                row += symbol
                col_num += 1
            return row

        def __str__(self):
            # generate the perimeter lines
            perimeter = self._draw_row(constant.PERIMETER_LINE)
            #generate the lines depicting space between rows
            grid_row = self._draw_row(constant.GRID_SQUARE_LINE)

            stringify_floor = perimeter
            stringify_floor += "\n"
            floor_row = 0
            while (floor_row < self.bounds):
                floor_column = 0
                stringify_floor += "|"
                while floor_column < self.bounds:
                    stringify_floor += (self.this_floor[floor_row][floor_column] + "|")
                    floor_column += 1
                stringify_floor += "\n"
                if(floor_row == self.bounds):
                    stringify_floor += perimeter
                else:
                    stringify_floor += grid_row
                    stringify_floor += "\n"
                    floor_row += 1
            return stringify_floor

        # Populates the dungeon floor with empty dungeon spaces
        def _create_floor(self):
            row_num = 0
            while row_num < self.bounds:
                self.this_floor.append(self._generate_empty_row())
                row_num += 1

        def _generate_empty_row(self):
            square_num = 0
            this_row = []
            while square_num < self.bounds:
                this_row.append(constant.EMPTY_SPACE)
                square_num += 1
            return this_row