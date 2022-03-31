
# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley




import pyray
import random
from game.cast.Monster.monsterpen import Monster_Pen
from game.cast.Players.house import House
from game.common.actions import Actions

class Director:
    
    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.game_over = False
        self.pen = Monster_Pen()
        self.monster = self.pen.get_current_monster()
        self.house = House()
        self.player = self.house.get_current_player()
        self.arena = Actions(self.player,self.monster)
        self.in_fight = False
        self.choice = ""
        self.current_turn = 0
        self.game_level = 1
        self.playing_game = True


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

        if self.in_fight == True:
            print("\nPick your action\n 1. attack\n 2. defend\n 3. heal\n\nPress enter to confirm")
            self.choice = input()



    def _do_updates(self):
        if self.in_fight == True:
            if self.current_turn == 0 and self.player.current_hp > 0:
                if self.choice == "1":
                    self.arena.attack()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
                if self.choice == "2":
                    self.arena.defend()
                if self.choice == "3":
                    self.arena.heal()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
            self.current_turn = 1
            if self.monster.current_hp < 1:
                self.game_level += 1
                self.player.stats.level = self.game_level
                self.player.stats.level_up()
                print(f"The {self.monster.name} Died\n")

                self.in_fight = False

            if self.current_turn == 1 and self.monster.current_hp > 0:

                monster_choice = random.randint(0,2)
                if monster_choice == 0:
                    self.arena.monster_attack()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
                    print(f"\nThe {self.monster.name} Attacked")

                if monster_choice == 1:
                    self.arena.monster_defend()
                    print(f"\nThe {self.monster.name} defended")

                if monster_choice == 2:
                    self.arena.monster_heal()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
                    print(f"\nThe {self.monster.name} Healed")
            self.current_turn = 0
            if self.player.current_hp < 1:
                self.playing_game = False
                self.in_fight = False

        if self.in_fight == False:
           
            self.player.current_hp = self.player.stats.get_health_points()
            self.pen.release_monster()
            self.monster = self.pen.get_current_monster()
            monster_level = self.game_level - 1
            self.monster.stats.level = monster_level
            if monster_level > 0:
                self.monster.stats.level_up()
            self.monster.current_hp = self.monster.stats.get_health_points()
            self.arena = Actions(self.player,self.monster)
            self.in_fight = True 
        

        

    def _do_outputs(self):
        self._video_service.clear_buffer()
        print(f"{self.player.name} has {self.player.current_hp} HP")
        print(f"{self.monster.name} has {self.monster.current_hp} HP\n")
        while self.playing_game == False:
            print ("Game Over")
        #self._video_service.draw_actors(actors)

        self._video_service.flush_buffer()
