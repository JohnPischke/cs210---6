
from game.common.location import Location
class Actor:

    def __init__(self):
        self._location = Location(x, y)
        self._symbol = "#"
        self._text_size = 50
        self._color = (0,0,0)
    
    def get_location (self):
        return self._location

    def get_symbol (self):
        return self._symbol

    def get_text_size (self):
        return self._text_size

    def get_color (self):
        return self._color

    def set_location (self, value):
        self._location = value

    def set_symbol (self, value):
        self._symbol = value

    def set_text_size (self, value):
        self._text_size = value

    def set_color (self, value):
        self._color = value
    