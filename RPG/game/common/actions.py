class Actions: 
    
    def __init__(self, doer, reciever): 
    self.doer_stats = doer.get_stats()

    self.doer_strength = doer_stats.get_strength
    self.doer_health = doer.get_current_hp
    self.doer_defense = doer_stats.get_defense
    self.doer_heal = doer_stats.get_heal


    self.doer_current_hp = doer.get_current_hp


    self.reciever_stats = reciever.get_stats()

    self.reciever_strength = reciever_stats.get_strength
    self.reciever_health = reciever.get_current_hp
    self.reciever_defense = reciever_stats.get_defense
    self.reciever_heal = reciever_stats.get_heal


    self.reciever_current_hp = reciever.get_current_hp

    # self.defense_enabled = 


    def attack(self): 
        self.reciever_current_hp -= self.doer_strength
        return self.reciever_current_hp

    def defend(self): 
        # not sure how to make the defend buttong only work once, and only when the player that is being attacked has done the defend action before. 

    def heal(self): 
        self.doer_current_hp += self.doer_heal          

    

        


    

        