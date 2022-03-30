
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley


import random

class Location:
    
    def __init__(self, x, y):
        self._point_x = x
        self._point_y = y

    def move(self, x, y):
        self._point_x += x
        self._point_y += y
        return (self._point_x, self._point_y)

    def get_location(self):
        return (self._point_x, self._point_y)

    def get_x(self):
        return self._point_x 
    
    def get_y(self):
        return self._point_y 
    
    def set_x(self, x):
        self._point_x = x
    
    def set_y(self, y):
        self._point_x = y
    
    def set_location(self, x,y):
        self._point_x = x
        self._point_y = y
        
    def scale(self, factor):
        return Location(self._point_x * factor, self._point_y * factor)