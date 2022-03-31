from game.cast.actor import Actor
from game.common.stats import Stats
from game.common.location import Location
class Wizard(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(250, 250)
        self._symbol = "?"
        self._text_size = 50
        self._color = (0,0,0)
        self.stats = Stats(3, 1, 1, 3)
        self.current_hp = 0
        self.name = "Wizard"

    def get_stats(self):
        return self.stats

    def get_current_hp(self):
        return self.current_hp
