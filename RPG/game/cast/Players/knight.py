from game.cast.actor import Actor
from game.common.skills import Skills
class Knight(Actor):

    def __init__(self):
        super().__init__()
        self._location = Location(x, y)
        self._symbol = "!>"
        self._text_size = 65
        self._color = (0,0,0)
        self.skills = Skills(,,,,)
        

    def get_skills():
        return self.skills
    