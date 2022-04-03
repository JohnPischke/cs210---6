# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley
''' This is the Action class. this class preforms actions by the player and monster'''
class Actions: 
    
    def __init__(self, doer, reciever): 
        self.doer = doer
        self.doer_stats = self.doer.get_stats()

        self.doer_strength = self.doer_stats.get_strength()
        self.doer_health = self.doer.get_current_hp()
        self.doer_defense = self.doer_stats.get_defense()
        self.doer_heal = self.doer_stats.get_heal()
        
        self.reciever = reciever
        self.reciever_stats = self.reciever.get_stats()

        self.reciever_strength = self.reciever_stats.get_strength()
        self.reciever_health = self.reciever.get_current_hp()
        self.reciever_defense = self.reciever_stats.get_defense()
        self.reciever_heal = self.reciever_stats.get_heal()
        self.doer_is_defending = False
        self.reciever_is_defending = False



    def attack(self): 
        self.doer_is_defending = False
        damage = 0
        if self.reciever_is_defending == True:
            damage = (self.doer_strength - (self.reciever_defense*2))
            if damage < 0:
                damage = 0
            self.reciever_health -= damage
            self.receiver_is_defending = False
        else:
            damage = (self.doer_strength - self.reciever_defense)
            if damage < 1:
                damage = 1
            self.reciever_health -= damage

    def defend(self): 
        self.doer_is_defending = True

    def heal(self): 
        self.doer_health += self.doer_heal
        self.doer_is_defending = False          

    def monster_attack(self): 
        self.reciever_is_defending = False
        damage = 0
        if self.doer_is_defending == True:
            damage = (self.reciever_strength - (self.doer_defense*2))
            if damage < 0:
                damage = 0
            self.doer_health -= damage
            self.doer_is_defending = False
        else:
            damage = (self.reciever_strength - self.doer_defense)
            if damage < 1:
                damage = 1
            self.doer_health -= damage

    def monster_defend(self): 
        self.reciever_is_defending = True
      
    def monster_heal(self): 
        self.reciever_health += self.reciever_heal        
        self.reciever_is_defending = False  


    

        


    

        