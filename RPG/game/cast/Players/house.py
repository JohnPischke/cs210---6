# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley
''' This is the house class. this class is in charge of creating a player class and giving it back'''

#from game.cast.Monster.cyclops import Cyclops
#from game.cast.Monster.demon import Demon
#from game.cast.Monster.dragon import Dragon
#from game.cast.Monster.harpy import Harpy
#from game.cast.Monster.hydra import Hydra
#from game.cast.Monster.kobold import Kobold
#from game.cast.Monster.medusa import Medusa
#from game.cast.Monster.minotaur import Minotaur
#from game.cast.Monster.spider import Spider
from game.cast.Players.knight import Knight
from game.cast.Players.archer import Archer
from game.cast.Monster.zombie import Zombie
from game.cast.Players.wizard import Wizard
import random
import pyray

class House():

    def __init__(self):
        self.house = []
        self.current_player = Zombie()

    def get_house(self):
        return self.house
    
    def get_current_player(self):
        return self.current_player

    def choose_class(self, answer):
            if answer == 1:
                self.current_player = Wizard()
            if answer == 2:
                self.current_player = Archer()
            if answer == 3:
                self.current_player = Knight()
   