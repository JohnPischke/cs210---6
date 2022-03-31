
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley




import pyray
import random
from game.cast.Monster.monsterpen import Monster_Pen
from game.cast.Players.house import House
#from game.common.actions import Actions

class Director:
    
    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.game_over = False
        self.pen = Monster_Pen()
        self.house = House()
        self.player = self.house.get_current_player()


    def start_game(self):
        self._video_service.open_window()
        self.pen.fill_pen()
        self.house.choose_class()
        self.player = self.house.get_current_player()
        self.game_loop()

    def game_loop(self):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._video_service.close_window()

    def _get_inputs(self):
        pass

    def _do_updates(self):
        print (self.player.name)
        self.pen.release_monster()
        monster = self.pen.get_current_monster()
        print (monster.name) 

        

    def _do_outputs(self):
        self._video_service.clear_buffer()
        
        #self._video_service.draw_actors(actors)

        self._video_service.flush_buffer()
