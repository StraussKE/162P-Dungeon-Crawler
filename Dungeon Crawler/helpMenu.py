import constant

class helpMenu(object):
    """User accessible help menu"""

    EXIT = 0,
    EX_DUNG = 1
    EX_MOVE = 2
    EX_TREAS = 3
    EX_STAIR = 4
    EX_TRAP = 5
    EX_ROCK = 6
    # EX_MONST = 8
    EX_PORT = 7

    MAX_VALID_OPTION = 7
    
    #include "validation.h"
    #include "text_tables.h"
    def __init__(self):
        # running
        self.runHelp = True
        self.pauseBar
        
    # Runs the help menu
    def openMenu(self):
        self.runHelp = True
        while self.runHelp:
    
            print(" Please select a topic from our help menu for clarification:\n"
                  "\t1 - |   |\tThe Dungeon\t|   |\n"
                  "\t2 - |   |\tMovement \t|   |\n"
                  "\t3 - |" + constant.TREASURE + "|\tTreasure \t|" + constant.KEY + "|\n"
                  "\t4 - |" + constant.STAIRS_DOWN + "|\tStairs \t\t|" + constant.STAIRS_UP + "|\n"
                  "\t5 - |" + constant.TRAP + "|\tTraps \t\t|" + constant.TRAP + "|\n"
                  "\t6 - |" + constant.SMALL_BOULDER + "|\tRocks \t\t|" + constant.LARGE_BOULDER + "|\n"
                  "\t7 - |" + constant.PORTAL + "|\tPortals \t|" + constant.PORTAL + "|\n"
                  "\n\t0 - Return to game\n\n")
    #not yet implemented
                #"\t7 - |" + constant.GOBLIN + "|\tMonsters \t|" + constant.ORC + "|\n"
            optionSelect = intInput(helpMenu.EXIT, helpMenu.MAX_VALID_OPTION)
            if (optionSelect == EXIT):
                print("\nFeel free to use the help menu again anytime you require. Happy adventuring!\n\n")
                self.runHelp = False
            elif (optionSelect == EX_DUNG):
                self.welcome()
            elif (optionSelect == EX_MOVE):
                self.aboutMovement()
            elif (optionSelect == EX_TREAS):
                self.aboutTreasure()
            elif (optionSelect == EX_STAIR):
                self.aboutStairs()
            elif (optionSelect == EX_TRAP):
                self.aboutTraps()
            elif (optionSelect == EX_ROCK):
                self.aboutBoulders()
            elif (optionSelect == EX_MONST):
                self.aboutMonsters()
            elif (optionSelect == EX_PORT):
                self.aboutPortals ()
            else:
                print("Error! I should not have been able to get here!.\n")
    
    # explains movement mechanics
    def aboutMovement (self):
        print("\nEach turn you may move a single square in one of the cardinal directions.\n"
              "Diagonal motion is not permitted.\n\n"
              "You have two options for controlling your character.\n\n"
              "Left handed control:\tW = up  A = left  S = down  D = right\n"
              "Right handed control:\t8 = up  4 = left  2 = down  6 = right\n\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains stair mechanics
    def aboutStairs (self):
        print("\nStairs allow you to travel between floors of the dungeon.\n\n"
              "|" + STAIRS_DOWN + "| indicates a downward stairway that will allow you to descend deeper\n"
              "into the dungeon.\n\n"
              "|" + STAIRS_UP + "| indicates an upward stairway that will allow you to return to floors\n"
              "previously explored.\n\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains about treasure and key mechanics
    def aboutTreasure (self):
        print("\n|" + KEY + "| Keys are required to open treasure chests.\n\n"
              "|" + TREASURE + "| Treasure chests are filled with gold for you to collect.\n\n"
              "Once you have collected a treasure, you will always be given the option to quit or continue\n"
              "exploring the dungeon.\n\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains about trap mechanics
    def aboutTraps (self):
        print("\n|" + TRAP + "| Traps are dangerous and you will die if you step in one.\n"
              "Avoid or disarm traps whenever possible.\n\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # small rock and boulder mechanics
    def aboutBoulders (self):
        print("\n|" + LARGE_BOULDER + "| Boulders are immobile obstacles that you must travel around.\n\n"
              "\n|" + SMALL_BOULDER + "| Small rocks can be pushed around and used to disarm traps.\n\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains monster mechanics NOT CURRENTLY IMPLEMENTED
#    def aboutMonsters (self):
#        about monsters

    # explains portal mechanics
    def aboutPortals (self):
        print("\n|" + PORTAL + "| Portals exist on the final floor of a dungeon. Stepping on the portal\n"
              "allows you to keep the treasure you've collected and continue on to another dungeon of\n"
              "whatever difficulty level you'd like.\n\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)