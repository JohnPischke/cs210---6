from game.cast.Players.player import Player
from game.common.skills import Skills
class Knight(Actor):

    def __init__(self, x, y):
        super().__init__(x,y)
        #self._location = Location(x, y)
        #self._symbol = "#"
        #self._text_size = 50
        self._color = (0,0,0)
        self.skills = Skills(,,,,)

    def get_skills():
        return self.skills
    