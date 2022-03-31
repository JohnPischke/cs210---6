class Stats: 
    def __init__(self, a, b, c, d): 
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.level = 1

        self.strength = (4 + a) * self.level
        self.health_points = (12 + b) * self.level
        self.defense = (2 + c) * self.level
        self.heal = (2 + d) * self.level


    def get_level(self): 
        return self.level

    def get_strength(self): 
        return self.strength

    def get_health_points(self): 
        return self.health_points

    def get_defense(self): 
        return self.defense
    
    def get_heal(self): 
        return self.heal

    def set_level(self, value):
        self.level = value

    def level_up(self):
        self.strength = (4 + (self.a * self.level))
        self.health_points = (12 + (self.b * self.level))
        self.defense = (2 + (self.c * self.level))
        self.heal = (2 + (self.d * self.level))
    
  