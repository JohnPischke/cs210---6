# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley
''' This is the keyboard service of the program. This detects key presses.'''


from game.common.location import Location
import pyray
class Keyboard_Service:
    
    def __init__(self, cell_size):
        self._cell_size = cell_size

   
    def get_direction(self):
        dx = 0

        if pyray.is_key_down(pyray.KEY_A):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_D):
            dx = 2

        if pyray.is_key_down(pyray.KEY_H):
            dx = 3

        if pyray.is_key_down(pyray.KEY_M):
            dy = 4

        # direction = direction.scale(self._cell_size)
        
        return dx