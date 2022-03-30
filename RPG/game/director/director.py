
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley




import pyray
import random
from game.casting.players import Player
from game.casting.player_1 import Player_1
from game.casting.player_2 import Player_2
from game.casting.trail_chunk import Trail_Chunk
from game.casting.trail import Trail

class Director:
    
    def __init__(self, keyboard_service, keyboard_service_2, video_service):
        self._keyboard_service = keyboard_service
        self._keyboard_service_2 = keyboard_service_2
        self._video_service = video_service
        self._cast = ""
        self.player = Player_1(100,300)
        self.player_2 = Player_2(800,300)
        self.velocity = (1,0)
        self.velocity_2 = (-1,0)
        self.trail = Trail()
        self.trail_2 = Trail()
        self.trail_color = (random.randrange(255), random.randrange(255),random.randrange(255))
        self.trail_2_color = (random.randrange(255), random.randrange(255),random.randrange(255))
        self.game_over = False


    def start_game(self):
        #self._cast = cast
        self.game_loop()

    def game_loop(self):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._video_service.close_window()

    def _get_inputs(self):
        player = self.player
        player_2 = self.player_2
        if self._keyboard_service.get_direction() != (0,0):

           self.velocity = self._keyboard_service.get_direction()
        if self._keyboard_service_2.get_direction() != (0,0):

            self.velocity_2 = self._keyboard_service_2.get_direction()

        player.move_x(self.velocity)
        player_2.move_x(self.velocity_2)
        pass

    def _do_updates(self):
        x = self.player.get_x()
        y = self.player.get_y()
        chunk = Trail_Chunk(x,y, self.trail_color[0],self.trail_color[1],self.trail_color[2])
        x_2 = self.player_2.get_x()
        y_2 = self.player_2.get_y()
        chunk_2 = Trail_Chunk(x_2,y_2,self.trail_2_color[0],self.trail_2_color[1],self.trail_2_color[2])
        self.trail.add_chunk(chunk)
        self.trail_2.add_chunk(chunk_2)
        player_1_location = self.player.get_location()
        player_2_location = self.player_2.get_location()
        for chunk in self.trail.trail_chunks:
            if chunk.location.get_location() == player_2_location.get_location():
                 self.game_over = True
        for chunk in self.trail_2.trail_chunks:
            if chunk.location.get_location() == player_1_location.get_location():
                 self.game_over = True
        if self.game_over == True:
            self.player.set_color((248,248,255))
            self.player_2.set_color((248,248,255))
                 

        

    def _do_outputs(self):
        self._video_service.clear_buffer()
        if self.game_over == True:
            pyray.draw_text(str("Game Over"), 80, 250, 150, (252,252,252))
        actors = self.trail.trail_chunks
        actors_2 = self.trail_2.trail_chunks
        self._video_service.draw_actor(self.player)
        self._video_service.draw_actor(self.player_2)
        self._video_service.draw_actors(actors)
        self._video_service.draw_actors(actors_2)
        self._video_service.flush_buffer()
