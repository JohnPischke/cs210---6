from game.cast.actor import Actor
from game.common.skills import Skills
class Archer(Actor):

    def __init__(self, x, y):
        super().__init__()
        self._location = Location(x, y)
        self._symbol = "-->"
        self._text_size = 50
        self._color = (0,0,0)
        self.skills = Skills(,,,,)

    def get_skills():
        return self.skills
    