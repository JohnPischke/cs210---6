from game.cast.actor import Actor
from game.common.stats import Stats
class Archer(Actor):

    def __init__(self, x, y):
        super().__init__()
        self._location = Location(250, 250)
        self._symbol = "-->"
        self._text_size = 50
        self._color = (0,0,0)
        self.stats = Stats(,,,,)
        self.current_hp = 0

    def get_stats(self):
        return self.stats

    def get_current_hp(self):
        return self.current_hp

    