from game.cast.actor import Actor
from game.common.stats import Stats
class Archer(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(250, 250)
        self._symbol = "?"
        self._text_size = 50
        self._color = (0,0,0)
        self.stats = Stats(,,,,)

    def get_skills():
        return self.skills