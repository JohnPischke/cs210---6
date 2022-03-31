from game.cast.Monster.cyclops import Cyclops
from game.cast.Monster.demon import Demon
from game.cast.Monster.dragon import Dragon
from game.cast.Monster.harpy import Harpy
from game.cast.Monster.hydra import Hydra
from game.cast.Monster.kobold import Kobold
from game.cast.Monster.medusa import Medusa
from game.cast.Monster.minotaur import Minotaur
from game.cast.Monster.spider import Spider
from game.cast.Monster.witch import Witch
from game.cast.Monster.yeti import Yeti
from game.cast.Monster.zombie import Zombie
from game.cast.Monster.monster import Monster

class Monster_Pen():

    def __init__(self):
        self.pen = []
        self.current_monster = Monster()

    def get_pen(self):
        return self.pen
    
    def get_current_monster(self):
        return self.current_monster

    def release_monster(self):
        self.current_monster = self.pen.pop()
    
    def fill_pen(self):
        for i in range(8):
            x = random.randint(1,12)
            if x == 1:
               monster = Cyclops()
               self.pen.append(monster)

            if x == 2:
               monster = Demon()
               self.pen.append(monster)

            if x == 10:
               monster = Dragon()
               self.pen.append(monster)

            if x == 11:
               monster = Harpy()
               self.pen.append(monster)

            if x == 3:
               monster = Hydra()
               self.pen.append(monster)

            if x == 4:
               monster = Kobold()
               self.pen.append(monster)

            if x == 5:
               monster = Medusa()
               self.pen.append(monster)

            if x == 6:
               monster = Minotaur()
               self.pen.append(monster)

            if x == 7:
               monster = Spider()
               self.pen.append(monster)

            if x == 12:
               monster = Witch()
               self.pen.append(monster)

            if x == 8:
               monster = Yeti()
               self.pen.append(monster)

            if x == 9:
               monster = Zombie()
               self.pen.append(monster)


