from game.cast.actor import Actor
from game.common.stats import Stats
class Monster(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(450, 250)
        self._symbol = "?"
        self._text_size = 50
        self._color = (0,0,0)
        self.stats = Stats(,,,,)
        self.current_hp = 0

    def get_stats(self):
        return self.stats

    def get_current_hp(self):
        return self.current_hp
