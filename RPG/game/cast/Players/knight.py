from game.cast.actor import Actor
from game.common.stats import Stats
class Knight(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(250, 250)
        self._symbol = "!>"
        self._text_size = 65
        self._color = (0,0,0)
        self.stats = Stats(2, 0, 2, 0)
        

    def get_stats():
        return self.stats
    