
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
        self.did_action = False
        self.asking_for_action = False
        self.monster_text = ""
        self.player_text =""


    def start_game(self):
        self._video_service.open_window()
        self._video_service.clear_buffer()
        self.pen.fill_pen()
        have_class = False
        while have_class == False:
            self._video_service.clear_buffer()
            #print ("choose your class\n A for wizard\n D for archer\n H for Knight\n")
            pyray.draw_text(str("choose your class\n A for wizard\n D for archer\n H for Knight\n"), 25, 25, 80, (252,252,252))
            answer = self._keyboard_service.get_direction()
            if answer == 1:
                have_class = True
            if answer == 2:
                have_class = True
            if answer == 3:
                have_class = True
            self._video_service.flush_buffer()
        self.house.choose_class(answer)
        self.player = self.house.get_current_player()
        self._video_service.clear_buffer()
        self._video_service.flush_buffer()

        self.game_loop()

    def game_loop(self):
        #self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._video_service.close_window()

    def _get_inputs(self):

        if self.in_fight == True:
            self.choice = 0
            #print("\nPick your action\n A. attack\n D. defend\n H. heal\n")
            
            #pyray.draw_text(str("\nPick your action\n A. attack\n D. defend\n H. heal\n"), 250, 250, 10, (252,252,252))
            self.choice = self._keyboard_service.get_direction()
            if self.choice != 0:
                self.did_action = True
           # self.choice = input()



    def _do_updates(self):
        if self.in_fight == True:
            if self.current_turn == 0 and self.player.current_hp > 0:
                if self.choice == 1:
                    self.arena.attack()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
                    self.player_text = "You Attacked"
                if self.choice == 2:
                    self.arena.defend()
                    self.player_text = "You Defended"
                if self.choice == 3:
                    self.arena.heal()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
                    self.player_text = "You Healed"
            if self.did_action == True:
                self.current_turn = 1
            if self.monster.current_hp < 1:
                self.game_level += 1
                self.player.stats.level = self.game_level
                self.player.stats.level_up()
                #print(f"The {self.monster.name} Died\n")

                self.in_fight = False

            if self.current_turn == 1 and self.monster.current_hp > 0:

                monster_choice = random.randint(0,2)
                if monster_choice == 0:
                    self.arena.monster_attack()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
                    self.did_action = False
                    self.monster_text = self.monster.name + " Attacked"
                   # print(f"\nThe {self.monster.name} Attacked")

                if monster_choice == 1:
                    self.arena.monster_defend()
                    self.did_action = False
                    self.monster_text = self.monster.name + " Defended"
                   # print(f"\nThe {self.monster.name} defended")

                if monster_choice == 2:
                    self.arena.monster_heal()
                    self.player.current_hp = self.arena.doer_health
                    self.monster.current_hp = self.arena.reciever_health
                    self.did_action = False
                    self.monster_text = self.monster.name + " Healed"
                  #  print(f"\nThe {self.monster.name} Healed")
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
       # print(f"{self.player.name} has {self.player.current_hp} HP")
        #print(f"{self.monster.name} has {self.monster.current_hp} HP\n")
        #self._video_service.draw_actor()
        pyray.draw_text(str("\nPick your action\n A. attack\n D. defend\n H. heal\n"), 300, 400, 25, (252,252,252))
        pyray.draw_text(str("Battle Arena!!!"), 200, 25, 60, (random.randrange(255), random.randrange(255),random.randrange(255)))
        pyray.draw_text(str("Level " + str(self.game_level)), 25, 25, 15, (252,252,252))
        pyray.draw_text(str("# of monsters left " + str(len(self.pen.get_pen()))), 725, 25, 15, (252,252,252))
        pyray.draw_text(str(self.player_text), 100, 100, 20, (252,252,252))
        pyray.draw_text(str(self.monster_text), 500, 100, 20, (252,252,252))
        pyray.draw_text(str( self.player.name + "'s Health: " + str(self.player.current_hp)), 100, 350, 20, (252,252,252))
        pyray.draw_text(str( self.monster.name + "'s Health: " + str(self.monster.current_hp)), 500, 350, 20, (252,252,252))
        self._video_service.draw_actor(self.player)
        self._video_service.draw_actor(self.monster)
        #pyray.draw_text(str("Game Over"), 80, 250, 150, (252,252,252))
        #while self.playing_game == False:
        # print ("Game Over")
        #self._video_service.draw_actors(actors)

        self._video_service.flush_buffer()
