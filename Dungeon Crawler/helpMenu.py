import constant
import validation

class helpMenu(object):
    """User accessible help menu"""

    EXIT = 0
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
        
    # Runs the help menu
    def open_menu(self):
        self.run_help = True
        while self.run_help:
    
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
            
            option_select = validation.int_input(helpMenu.EXIT, helpMenu.MAX_VALID_OPTION)

            if (option_select == helpMenu.EXIT):
                print("\nFeel free to use the help menu again anytime you require. Happy adventuring!\n\n")
                self.runHelp = False
            elif (option_select == helpMenu.EX_DUNG):
                self.welcome()
            elif (option_select == helpMenu.EX_MOVE):
                self.about_movement()
            elif (option_select == helpMenu.EX_TREAS):
                self.about_treasure()
            elif (option_select == helpMenu.EX_STAIR):
                self.about_stairs()
            elif (option_select == helpMenu.EX_TRAP):
                self.about_traps()
            elif (option_select == helpMenu.EX_ROCK):
                self.about_boulders()
            #elif (option_select == helpMenu.EX_MONST):
            #    self.aboutMonsters()
            elif (option_select == helpMenu.EX_PORT):
                self.about_portals ()
            else:
                print("Error! I should not have been able to get here!.\n")

    # Welcomes user to the game and explains the purpose of the game
    def welcome(self):
        print("\t __          ________ _      _____ ____  __  __ ______\n"
              "\t \\ \\        / /  ____| |    / ____/ __ \\|  \\/  |  ____|\n"
              "\t  \\ \\  /\\  / /| |__  | |   | |   | |  | | \\  / | |__ \n"
              "\t   \\ \\/  \\/ / |  __| | |   | |   | |  | | |\\/| |  __|\n"
              "\t    \\  /\\  /  | |____| |___| |___| |__| | |  | | |____\n"
              "\t     \\/  \\/   |______|______\\_____\\____/|_|  |_|______|\n"
              "\t             | |        | | | |\n"
              "\t             | |_ ___   | |_| |__   ___\n"
              "\t             | __/ _ \\  | __| '_ \\ / _ \\\n"
              "\t             | || (_) | | |_| | | |  __/\n"
              "\t     _____  _ \\__\\___/ _ \\__|_| |_|\\___|___  _   _\n"
              "\t    |  __ \\| |  | | \\ | |/ ____|  ____/ __ \\| \\ | |\n"
              "\t    | |  | | |  | |  \\| | |  __| |__ | |  | |  \\| |\n"
              "\t    | |  | | |  | | . ` | | |_ |  __|| |  | | . ` |\n"
              "\t    | |__| | |__| | |\\  | |__| | |___| |__| | |\\  |\n"
              "\t    |_____/ \\____/|_| \\_|\\_____|______\\____/|_| \\_|\n\n")

    # ascii art generated by http://patorjk.com/software/taag/
    # formatting to output in C++/Python done personally

        print(" This dungeon endeavors to evoke a sense of adventure and nostalgia reminiscent\n"
                " of the text based adventures of yore.  You are the hero.  Your purpose is to\n"
                " avoid death and collect treasure.  The story is regrettably lacking.  This is\n"
                " a roguelike game with a fixed quantity of floors for you to enjoy.\n"
                " Now that you understand the premise, let us be on our way!\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)
    
                
                
    # explains movement mechanics
    def about_movement (self):
        print("\nEach turn you may move a single square in one of the cardinal directions.\n"
              "Diagonal motion is not permitted.\n\n"
              "You have two options for controlling your character.\n\n"
              "Left handed control:\tW = up  A = left  S = down  D = right\n"
              "Right handed control:\t8 = up  4 = left  2 = down  6 = right\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains stair mechanics
    def about_stairs (self):
        print("\nStairs allow you to travel between floors of the dungeon.\n\n"
              "|" + constant.STAIRS_DOWN + "| indicates a downward stairway that will allow you to descend deeper\n"
              "into the dungeon.\n\n"
              "|" + constant.STAIRS_UP + "| indicates an upward stairway that will allow you to return to floors\n"
              "previously explored.\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains about treasure and key mechanics
    def about_treasure (self):
        print("\n|" + constant.KEY + "| Keys are required to open treasure chests.\n\n"
              "|" + constant.TREASURE + "| Treasure chests are filled with gold for you to collect.\n\n"
              "Once you have collected a treasure, you will always be given the option to quit or continue\n"
              "exploring the dungeon.\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains about trap mechanics
    def about_traps (self):
        print("\n|" + constant.TRAP + "| Traps are dangerous and you will die if you step in one.\n"
              "Avoid or disarm traps whenever possible.\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # small rock and boulder mechanics
    def about_boulders (self):
        print("\n|" + constant.LARGE_BOULDER + "| Boulders are immobile obstacles that you must travel around.\n\n"
              "\n|" + constant.SMALL_BOULDER + "| Small rocks can be pushed around and used to disarm traps.\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)

    # explains monster mechanics NOT CURRENTLY IMPLEMENTED
#    def aboutMonsters (self):
#        about monsters

    # explains portal mechanics
    def about_portals (self):
        print("\n|" + constant.PORTAL + "| Portals exist on the final floor of a dungeon. Stepping on the portal\n"
              "allows you to keep the treasure you've collected and continue on to another dungeon of\n"
              "whatever difficulty level you'd like.\n")
        input("(Press enter to continue)")
        print(constant.STARBAR)