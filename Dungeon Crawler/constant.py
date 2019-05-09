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
BOULDER_BLOCK = 'The solemn boulder stands eternal sentinel here. You can not pass.\n'
TRAP_TRIGGER = "Horrible things happen.  You die.  Game over.  I'm sad, really. \n"


# Dictionaries

TRAP_DISARM = {
    0 : "a sudden eruption of fire incinerates your boulder.\n",
    1 : "your boulder drops into a newly exposed acid vat.\n",
    2 : "monstrous scythes drop from above and split your boulder.\n",
    3 : "something underwhelming happens.\n"}

HIT_WALL_BOULDER = {
    0 : "Your efforts to shove the small boulder through the wall are met with resistance\n Please try something else.\n",
    1 : "You are unable to achieve enough force to embed the bounder into the wall.\n Please try something else.\n",
    2 : "You have chosen to attempt something improbable with the boulder.  It failed.\n"}

HIT_WALL_PLAYER = {
    0: "With feline stealth the exterior wall suddenly appears in front of you.\nPlease try something else.\n",
    1: "Your jaunty step is thrown off by an abrupt encounter with a sturdy wall.\nPlease try something else.\n",
    2: "Despite your efforts to prove otherwise, the wall is not an illusion.\nPlease try something else.\n",
    3: "Your quixotic effort to slay the wall has only gained you shame.\nPlease try something else.\n"}

BOULDER_PLAY = {
    PLAYER : ("You begin to enter a room but are unable to bypass a small boulder. It appears\n" +
              "that you can carry it, barely. Would you like to carry the boulder?\n"),
    TRAP : ("After straining to move your boulder around for what seems an eternity, your\n" +
            "diligence is rewarded as you shove it into the next room. A resounding click\n" +
            "is the only warning before "),
    STAIRS_UP : ("You attempt to carry the boulder up the stairs but discover yourself extremely\n" +
                 "lacking in the strength category. Humiliated you vow to exercise rigorously...\n" +
                 "Eventually.\n"),
    KEY : ("You hear the dismaying sound of breaking metal as you set your boulder down to\n" +
           "rest a moment. Lifting it back up with trepidation you discover the mangled\n" +
           "remains of a key.\n"),
    TREASURE : ("Peering around your boulder as best you can you spy the gleam of a treasure\n" +
                "chest in your intended direction. Taking a moment to reflect upon the chances\n" +
                "of the chest surviving contact with your boulder you reconsider your plans.\n"),
    LARGE_BOULDER : ("You see a boulder of such proportions as to dwarf the one you are currently\n" +
                    "struggling to carry. You retreat before your boulder can become envious of its\n" +
                    " bigger brother.\n"),
    SMALL_BOULDER : ("You attempt to progress forward but find your progress impeded. When you set\n" +
                     "your boulder down to discover the cause you discover it pressed close against\n" +
                     "it's twin. You realize with some sorrow that if you wish to go this way you will\n" +
                     "first have to be rid of your beloved boulder.\n"),
    PORTAL : ("As you enter the portal your faithful boulder friend disintegrates. You feel\n" +
              "unexpectedly lonely without the companionship.\n")}