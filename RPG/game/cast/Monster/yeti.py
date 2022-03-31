import random
from game.cast.actor import Actor
from game.common.stats import Stats
from game.common.location import Location
class Yeti(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(450, 250)
        self._symbol = "Y"
        self._text_size = 50
        self._color = (0,0,0)
        self.stats = Stats(random.randint(0, 6),random.randint(0, 6),random.randint(0, 6),random.randint(0, 6))
        self.current_hp = 0
        self.name = "Yeti"


    def get_stats(self):
        return self.stats

    def get_current_hp(self):
        return self.current_hp
    
    def level_up (self, level):
        self.stats.set_level(self.stats.get_level() + level)
