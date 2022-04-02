from game.cast.actor import Actor
from game.common.stats import Stats
from game.common.location import Location
class Archer(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(150, 150)
        self._symbol = "A"
        self._text_size = 200
        self._color = (0,201,87)
        self.stats = Stats(2,2,3,2)
        self.current_hp = 0
        self.name = "Archer"

    def get_stats(self):
        return self.stats

    def get_current_hp(self):
        return self.current_hp

    