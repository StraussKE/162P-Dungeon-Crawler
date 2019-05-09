import constant

class player(object):
    """description of class"""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.gold = 0
        self.key = 0
        self.dynamite = 0

    def __str__(self):
        return constant.PLAYER