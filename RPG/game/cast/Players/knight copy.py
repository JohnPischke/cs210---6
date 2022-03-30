from game.cast.actor import Actor
from game.common.stats import Stats
class Knight(Actor):

    def __init__(self, x, y):
        super().__init__(x,y)
        #self._location = Location(x, y)
        #self._symbol = "#"
        #self._text_size = 50
        self._color = (0,0,0)
        self.stats = Stats(,,,,)

    def get_skills():
        return self.skills
    