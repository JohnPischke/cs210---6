# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



from game.common.location import Location
import pyray
class Keyboard_Service:
    
    def __init__(self, cell_size):
        self._cell_size = cell_size

   
    def get_direction(self):
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_1):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_2):
            dx = 1

        if pyray.is_key_down(pyray.KEY_3):
            dy = -1

        if pyray.is_key_down(pyray.KEY_4):
            dy = 1

        direction = (dx , dy )
        # direction = direction.scale(self._cell_size)
        
        return direction