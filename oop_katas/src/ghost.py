import math
class Ghost:
    def __init__(self, name, speed, colour):
        self.name = name
        self.speed = speed
        self.colour = colour
    
    def is_scared(self):
        return False if self.colour != 'blue' else True

    def can_be_eaten(self):
        return False if self.is_scared() == False else True

    def frighten(self):
        self.colour = 'blue'
        pass

    def speed_up(self):
        self.speed = round(self.speed * 1.1, 3)

class Blinky(Ghost):
    pass

class Pinky(Ghost):
    pass

class Inky(Ghost):
    pass

class Clyde(Ghost):
    pass
    

