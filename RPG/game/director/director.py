
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley




import pyray
import random

class Director:
    
    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.game_over = False


    def start_game(self):
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
        pass
                 

        

    def _do_outputs(self):
        self._video_service.clear_buffer()
        
        #self._video_service.draw_actors(actors)

        self._video_service.flush_buffer()
