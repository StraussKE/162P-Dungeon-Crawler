# Created by Katie Strauss May 2019

# standard modules
import random

#user created modules
import constant
import validation
import helpMenu

class dungeon(object):
    """the dungeon being explored"""

    # initializes dungeon object
    def __init__(self):
        self.current_difficulty = self._set_difficulty()        # sets the dungeon difficulty level by calling setter
        
        self.bounds = self._set_bounds(self.current_difficulty) # sets the dungoun boundaries based on selected dificulty level
        self.dungeon = []                                       # initializes dungeon list
        self.current_floor = 0                                  # initializes display floor

        self._create_dungeon()                                  # creates dungeon as directed
        
        if (self.current_difficulty == constant.TUTORIAL):      # creates tutorial if selected
            self._create_tutorial()

    # directs how the dungeon should be printed, when a string representation is called for
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

    # interactive method to determine dungeon difficulty
    def _set_difficulty(self):
        print("\nPlease select your difficulty level. If you've never played before the tutorial\n"
            + "is highly recommended for explaining basic commands and mechanics. If you ever \n"
            + "need to review anything while exploring, just access our help menu by pressing H\n"
            + "\t" + str(constant.TUTORIAL) + ": Tutorial\n"
            + "\t" + str(constant.EASY) + ": Easy\n"
            + "\t" + str(constant.NORMAL) + ": Normal\n"
            + "\t" + str(constant.HARD) + ": Hard\n")
        return validation.int_input(1,4)

    # sets the bounds based on difficulty level
    def _set_bounds(self, difficulty):
        if(difficulty == constant.TUTORIAL):
            return constant.TUTORIAL_DIMENSION
        if(difficulty == constant.EASY):
            return constant.EASY_DIMENSION
        if(difficulty == constant.NORMAL):
            return constant.NORMAL_DIMENSION_MAX
        if(difficulty == constant.HARD):
            return constant.HARD_DIMENSION_MAX
    
    # generates a tutorial dungeon
    def _create_tutorial(self):
        qty_stairs_down = 1
        qty_treasure = 1
        qty_key = 1
        qty_traps = 1
        qty_small_rock = 1
        qty_boulder = 1
        qty_portal = 1

        self.dungeon[0]._update_square(0, 0, constant.PLAYER)                   # Place player at starting locaiton
        
        floor = 0
        while (floor < self.bounds - 1):
            self.dungeon[0]._place_object(qty_stairs_down, constant.STAIRS_DOWN)         # Place downward stairs where logical
        
        # Place 2nd floor tutorial objects
        self.dungeon[1]._place_object(sty_treasure, constant.TREASURE)          # Place treasure on 2nd floor
        self.dungeon[1]._place_object(qty_key, constant.KEY)                    # Place key on 2nd floor
        # Place 3rd floor tutorial objects
        self.dungeon[2]._place_object(qty_traps, constant.TRAP)                 # Place trap on 3rd floor
        self.dungeon[2]._place_object(qty_small_rock, constant.SMALL_BOULDER)   # Place small rock on 3rd floor
        self.dungeon[2]._place_object(qty_boulder, constant.BOULDER)            # Place small rock on 3rd floor
        # Place 4th floor tutorial objects
        self.dungeon[3]._place_object(qty_portal, constant.PORTAL)              # Place portal on final floor
        
    # creates dungeon
    def _create_dungeon(self):
        floor_num = 0
        while floor_num < self.bounds:
            self.dungeon.append(self.dungeon_floor(self.bounds, floor_num))
            floor_num += 1

    # generates an individual dungeon floor
    class dungeon_floor(object):
        def __init__(self, bounds, floor_number):
            self.bounds = bounds
            self.this_floor = []

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

        # places items in random locations
        def _place_object(self, quantity, symbol):
            random.seed()
            count = 0
            
            for count in range(0, quantity):
                x_axis = (random.randint(0, (self.bounds - 1)))
                y_axis = (random.randint(0, (self.bounds - 1)))

# fix me!                if (symbol != TREASURE and
# fix me!                           validation.too_close(dungeon, current_floor, bounds, x_axis, y_axis, constant.TREASURE)):
# fix me!                    count -= 1
# fix me!                elif ( dungeon[self.this_floor][y_axis][x_axis] != EMPTY_SPACE or
# fix me!                      validation.too_close(dungeon, self.this_floor, self.bounds, x_axis, y_axis, constant.PLAYER) or
# fix me!                      validation.too_close(dungeon, self.this_floor, self.bounds, x_axis, y_axis, constant.STAIRS_DOWN) or
# fix me!                      validation.too_close(dungeon, self.this_floor, self.bounds, x_axis, y_axis, constant.PORTAL)):
                # if there's already something there, don't put a trap there, try again
                # if it's out of bounds, don't attempt to put a trap there, try again
                # if it's too close to the treasure (within 1 square), don't put a trap there, try again
                # if it's too close to the player's starting point, don't put a trap there, try again
                # the purpose of the buffer around player and treasure is to minimize the likelihood of an unwinnable game due to random generation
# fix me!                    count -=1
# fix me!                else:
                self._update_square(x_axis, y_axis, symbol)

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

        # places an item in a specific location
        def _update_square(self, x, y, symbol):
            self.this_floor[y][x] = symbol