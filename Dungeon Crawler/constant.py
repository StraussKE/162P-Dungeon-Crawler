### Declaration of constant values for this application ###

## constant Integers

# Maximumn dimension for a dungeon
MAX_SIZE                = 19

# Beginning coordinate for Player
START_POINT             = 0

# Difficulty levels
TUTORIAL                = 1
EASY                    = 2
NORMAL                  = 3
HARD                    = 4

# Movement Codes
NORTH                   = 0
WEST                    = 1
SOUTH                   = 2
EAST                    = 3

# Other features accessible during movement phase
QUIT                    = 4
HELP                    = 5
RID_BOULDER             = 6

# Basic dungeon dimensions
TUTORIAL_DIMENSION      = 4
EASY_DIMENSION          = 8
NORMAL_DIMENSION_MAX    = 13
HARD_DIMENSION_MAX      = 19

## Constand Strings

GRID_SQUARE_LINE        = "- -|"
PERIMETER_LINE          = "---|"
EMPTY_SPACE             = "   "
TRAP                    = "<X>"
TREASURE                = "[T]"
KEY                     = "[K]"
STAIRS_DOWN             = "Dwn"
STAIRS_UP               = "Prv"
#  GOBLIN                  = "-_-"     // not currently implemented, requires behavioral algorithm (random movements)
#  ORC                     = "o_o",    // not currently implemented, requires behavioral algorithm (always moves toward player)
#  MERCHANT                = "$M$",    // not currently implemented, requires inventory, loot tables, character stats, etc.
LARGE_BOULDER           = "{B}"
SMALL_BOULDER           = "{b}"
PORTAL                  = "(@)"
PLAYER                  = "You"

## Building the dungeon

## constant Characters

## navigating a single floor of the dungeon

# Ascending or descending stairs
UP                      = 'U'
DOWN                    = 'D'

# Empty character
EMPTY                   = '\0'

# Text outputs

STARBAR = '*******************************************************************************\n'