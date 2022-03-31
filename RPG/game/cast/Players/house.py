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

    def choose_class(self):
        have_class = False
        while have_class == False:
            print ("choose your class\n 1 for wizard\n 2 for archer\n 3 for Knight\n\n Press enter to confirm")
            answer = input()
            if answer == "1":
                self.current_player = Wizard()
                have_class = True
            if answer == "2":
                self.current_player = Archer()
                have_class = True
            if answer == "3":
                self.current_player = Knight()
                have_class = True
   