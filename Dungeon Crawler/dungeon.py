# Created by Katie Strauss May 2019

# standard modules
import random

#user created modules
import constant
import validation
import helpMenu
import player


class dungeon(object):
    """the dungeon being explored"""
    
    # initializes dungeon object
    def __init__(self, player):
        self.this_player = player
        random.seed()
        self.current_difficulty = self._set_difficulty()        # sets the dungeon difficulty level by calling setter
        
        self.bounds = self._set_bounds(self.current_difficulty) # sets the dungoun boundaries based on selected dificulty level
        self.dungeon = []                                       # initializes dungeon list 
        
        if (self.current_difficulty == constant.TUTORIAL):      # creates tutorial if selected
            self._create_tutorial()
        else :
            self._create_dungeon()                               # creates dungeon as directed

    # directs how the dungeon should be printed, when a string representation is called for
    def __str__(self):
        if (self.dungeon[self.this_player.z].run_tutorial == True):
            self.dungeon[self.this_player.z].run_tutorial = self.this_player.run_tutorial()
        stringify_dung = constant.STARBAR
        stringify_dung += ("You are on level " + str(self.this_player.z + 1) + " of the dungeon.\n")
        stringify_dung += (constant.STARBAR + "\n")
        stringify_dung += str(self.dungeon[self.this_player.z])
        stringify_dung += constant.DUNG_KEY
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
    
    # Moves an object
    def move_target (self):
        # Creates test cordinates based on movement
        movement = self.this_player.movement()
        print("player x = " + str(self.this_player.x) + " player y = " + str(self.this_player.y))
        test_x = self.this_player.x
        test_y = self.this_player.y
        if (movement == constant.QUIT):
            return True
        elif (movement == constant.NORTH):
            test_y -= 1
        elif (movement == constant.SOUTH):
            test_y += 1
        elif (movement == constant.WEST):
            test_x -= 1
        elif (movement == constant.EAST):
            test_x += 1
        elif (movement == constant.RID_BOULDER):
            print("you got rid of a boulder!")
        else:
            raise ValueError
        
        if (self.dungeon[self.this_player.z].out_of_bounds(test_x, test_y) == False):
            if (self.dungeon[self.this_player.z].checkMove(test_x, test_y)):
                if (self.this_player.on_stairs == "down"):
                    self.dungeon[self.this_player.z].update_square(self.this_player.x, self.this_player.y, test_x, test_y, constant.STAIRS_DOWN)
                    self.this_player.on_stairs = "false"
                elif (self.this_player.on_stairs == "up"):
                    self.dungeon[self.this_player.z].update_square(self.this_player.x, self.this_player.y, test_x, test_y, constant.STAIRS_UP)
                    self.this_player.on_stairs = "false"
                else:
                    self.dungeon[self.this_player.z].update_square(self.this_player.x, self.this_player.y, test_x, test_y)
                print("player x = " + str(self.this_player.x) + " player y = " + str(self.this_player.y))
            elif (self.dungeon[self.this_player.z].checkMove(test_x, test_y, constant.STAIRS_UP)):
                self.this_player.z -= 1
                self.dungeon[self.this_player.z].update_square(self.this_player.x, self.this_player.y, test_x, test_y)
                self.this_player.on_stairs = "down"
            elif (self.dungeon[self.this_player.z].checkMove(test_x, test_y, constant.STAIRS_DOWN)):
                self.this_player.z += 1
                self.dungeon[self.this_player.z].update_square(self.this_player.x, self.this_player.y, test_x, test_y)
                self.this_player.on_stairs = "up"
            else:
                print("I don't yet know how to deal with this")
            self.this_player.x = test_x
            self.this_player.y = test_y
        else:
            splat = random.randint(0,3)
            print(constant.HIT_WALL_PLAYER[splat])

    # generates a tutorial dungeon
    def _create_tutorial(self):
        qty_stairs_down = 1
        qty_treasure = 1
        qty_key = 1
        qty_traps = 1
        qty_small_rock = 1
        qty_boulder = 1
        qty_portal = 1
        tutorial = True
        self._create_dungeon(tutorial)
        self.dungeon[0]._place_object(1, self.this_player)                          # Place this_player at starting location
        
        for floor in range(0, 3):
            self.dungeon[floor]._place_object(qty_stairs_down, constant.STAIRS_DOWN)# Place downward stairs where logical
        
        # Place 2nd floor tutorial objects
        self.dungeon[1]._place_object(qty_treasure, constant.TREASURE)              # Place treasure on 2nd floor
        self.dungeon[1]._place_object(qty_key, constant.KEY)                        # Place key on 2nd floor
        # Place 3rd floor tutorial objects
        self.dungeon[2]._place_object(qty_traps, constant.TRAP)                     # Place trap on 3rd floor
        self.dungeon[2]._place_object(qty_small_rock, constant.SMALL_BOULDER)       # Place small rock on 3rd floor
        self.dungeon[2]._place_object(qty_boulder, constant.LARGE_BOULDER)          # Place large rock on 3rd floor
        # Place 4th floor tutorial objects
        self.dungeon[3]._place_object(qty_portal, constant.PORTAL)                  # Place portal on final floor
        
    # creates dungeon
    def _create_dungeon(self, tutorial = False):
        floor_num = 0
        while floor_num < self.bounds:
            self.dungeon.append(self.dungeon_floor(self.bounds, floor_num, tutorial))
            floor_num += 1

    # generates an individual dungeon floor
    class dungeon_floor(object):
        def __init__(self, bounds, floor_number, tutorial):
            self.bounds = bounds
            self.run_tutorial = tutorial
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
                while floor_column < (self.bounds - 1):
                    stringify_floor += (str(self.this_floor[floor_row][floor_column]) + " ")
                    floor_column += 1
                stringify_floor += (str(self.this_floor[floor_row][floor_column]) + "|\n")
                if(floor_row == (self.bounds-1)):
                    stringify_floor += perimeter
                    floor_row += 1
                else:
                    stringify_floor += grid_row
                    stringify_floor += "\n"
                    floor_row += 1
            return stringify_floor

        #accepts the (x,y) coordinates for the intended move or object placement
        #checks to see if coordinates are within the limits of the array
        #returns true if coordinates exceed the set bounds, returns false if the coordinates fall within the acceptable range
        def out_of_bounds (self, proposed_x, proposed_y):
            if (proposed_x >= self.bounds or proposed_x < 0 or proposed_y >= self.bounds or proposed_y < 0):
                return True
            return False

        # Checks to see if square being moved to is viable option
        def checkMove (self, position_x, position_y, target_object = constant.EMPTY_SPACE):
            if (target_object == constant.EMPTY_SPACE):
                if (self.this_floor[position_y][position_x] != target_object):
                    # Not_empty
                    return False
                else:
                    # Empty
                    return True
            elif (self.this_floor[position_y][position_x] == target_object):
                # Not empty
                if(target_object == constant.STAIRS_UP):
                    print("stairs")
                return True
            else:
                # empty
                return False
        
        #accepts layout of the current floor of the dungeon, and the proposed x and y coordinates as well as the object being looked for
        #tests to see if proposed placement is within one square of designated test object
        #returns true if object is within one space, returns false if object is not within one space
        def _too_close (self, proposed_x, proposed_y, target_object):
            if (self.out_of_bounds(proposed_x + 1, proposed_y) == False and self.checkMove(proposed_x + 1, proposed_y, target_object) == True):
                return True
            elif(self.out_of_bounds(proposed_x - 1, proposed_y) == False and self.checkMove(proposed_x - 1, proposed_y, target_object) == True):
                return True
            elif(self.out_of_bounds(proposed_x, proposed_y + 1) == False and self.checkMove(proposed_x, proposed_y + 1, target_object) == True):
                return True
            elif(self.out_of_bounds(proposed_x, proposed_y - 1) == False and self.checkMove(proposed_x, proposed_y - 1, target_object) == True):
                return True
            else:
                return False

        # places items in random locations
        def _place_object(self, quantity, symbol):
            
            count = 0
            
            for count in range(0, quantity):
                x_axis = (random.randint(0, (self.bounds - 1)))
                y_axis = (random.randint(0, (self.bounds - 1)))
                if (self.this_floor[y_axis][x_axis] == constant.EMPTY_SPACE):
                    #if (self._too_close(x_axis, y_axis, constant.STAIRS_DOWN)):
                    #    count -= 1
                    #else:
                        self.this_floor[y_axis][x_axis] = symbol
                        if (str(symbol) == constant.PLAYER):
                            symbol.x = x_axis
                            symbol.y = y_axis
                else:
                    count -= 1

# fix me!                if (symbol != TREASURE and
# fix me!                           _too_close(dungeon, this_player.z, bounds, x_axis, y_axis, constant.TREASURE)):
# fix me!                    count -= 1
# fix me!                elif ( dungeon[self.this_floor][y_axis][x_axis] != EMPTY_SPACE or
# fix me!                      _too_close(dungeon, self.this_floor, self.bounds, x_axis, y_axis, constant.PLAYER) or
# fix me!  // fixed            _too_close(dungeon, self.this_floor, self.bounds, x_axis, y_axis, constant.STAIRS_DOWN) or
# fix me!                      _too_close(dungeon, self.this_floor, self.bounds, x_axis, y_axis, constant.PORTAL)):
                # if there's already something there, don't put a trap there, try again
                # if it's out of bounds, don't attempt to put a trap there, try again
                # if it's too close to the treasure (within 1 square), don't put a trap there, try again
                # if it's too close to the this_player's starting point, don't put a trap there, try again
                # the purpose of the buffer around this_player and treasure is to minimize the likelihood of an unwinnable game due to random generation
# fix me!                    count -=1
# fix me!                else:

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
        def update_square(self, old_x, old_y, new_x, new_y, leave_behind = constant.EMPTY_SPACE):
            self.this_floor[new_y][new_x] = self.this_floor[old_y][old_x]
            self.this_floor[old_y][old_x] = leave_behind