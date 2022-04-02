from game.cast.actor import Actor
from game.common.stats import Stats
from game.common.location import Location
class Knight(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(150, 150)
        self._symbol = "K"
        self._text_size = 200
        self._color = (255,48,48)
        self.stats = Stats(2, 4, 2, 1)
        self.name = "Knight"
        self.current_hp = 0

    def get_stats(self):
        return self.stats

    def get_current_hp(self):
        return self.current_hp
