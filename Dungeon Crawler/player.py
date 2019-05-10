import constant
from helpMenu import helpMenu

class player(object):
    """player object"""

    def __init__(self):
        self.playing = True
        self.on_stairs = "false"
        self.bouler = False
        
        self.x = 0
        self.y = 0
        self.z = 0
        
        self.gold = 0
        self.key = 0
        self.dynamite = 0

        self.helper = helpMenu()
        self.helper.welcome()

    def __str__(self):
        return constant.PLAYER

    def movement (self):
        while (True):
            movement = input()
            if (movement == 'Q' or movement == 'q'):
               self.playing = False
               return constant.QUIT
            elif (movement =='H' or movement == 'h'):
                self.helper.open_menu()
            elif (movement == 'A' or movement == 'a' or movement == '4'):
                return constant.WEST
            elif (movement == 'W' or movement == 'w' or movement == '8'):
                return constant.NORTH
            elif (movement == 'D' or movement == 'd' or movement == '6'):
                return constant.EAST
            elif (movement == 'S' or movement == 's' or movement == '2'):
                return constant.SOUTH
            elif (movement == 'R' or movement == 'r'):
                return constant.RID_BOULDER
            else:
                print("You have selected an invalid option.")
                self.helper.about_movement()
                print("Please select a valid option now.")

    def run_tutorial(self):
        if (self.z == 0):
            self.helper.about_movement()
            self.helper.about_stairs()
            print("Why don't you try getting to the stairs on this floor?\n")
            return False
        if (self.z == 1):
            self.helper.about_treasure()
            print("Why don't you try getting the treasure from this floor?\n")
            return False
        if (self.z == 2):
            self.helper.about_traps()
            self.helper.about_boulders()
            print("Why don't you try disarming the trap on this floor?\n")
            return False
        if (self.z == 3):
            self.helper.about_portals()
            print("Head through the portal to finish this tutorial.\n")
            return False