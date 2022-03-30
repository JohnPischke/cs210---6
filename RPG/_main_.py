# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley

from game.director.director import Director
from game.services.video_service import Video_Service
from game.services.keyboard_service import Keyboard_Service
from game.services.keyboard_service_2 import Keyboard_Service_2

FRAME_RATE = 50
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = 'Cycle'


def main():
    # start the game
    
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)

    video_service = Video_Service(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    keyboard_service = Keyboard_Service(CELL_SIZE)
    keyboard_service_2 = Keyboard_Service_2(CELL_SIZE)
    director = Director(keyboard_service, keyboard_service_2, video_service)
    director.start_game()


if __name__ == '__main__':
    main()
