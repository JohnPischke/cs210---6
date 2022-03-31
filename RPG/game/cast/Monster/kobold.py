import random
from game.cast.actor import Actor
from game.common.stats import Stats
from game.common.location import Location
class Kobold(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(450, 250)
        self._symbol = "K"
        self._text_size = 50
        self._color = (random.randrange(255), random.randrange(255),random.randrange(255))
        self.stats = Stats(random.randint(0,2),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2))
        self.current_hp = 0
        self.name = "Kobold"


    def get_stats(self):
        return self.stats

    def get_current_hp(self):
        return self.current_hp
    
    def level_up (self, level):
        self.stats.set_level(self.stats.get_level() + level)
