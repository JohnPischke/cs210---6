# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley

from game.director.director import Director
from game.service.video_service import Video_Service
from game.service.keyboard_service import Keyboard_Service


FRAME_RATE = 5
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = 'RPG'


def main():
    # start the game
    
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)

    video_service = Video_Service(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    keyboard_service = Keyboard_Service(CELL_SIZE)
    director = Director(keyboard_service, video_service)
    director.start_game()


if __name__ == '__main__':
    main()
