from game_classes import fighter #grabbing the whole module fighter.Fighter
from game_classes.fighter import Fighter, Example #only grabbing the FIghter class from the module fighter

class Viking(Fighter):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.strength = 13
        self.speed = 8
        self.special = "pillage"
        self.buff = "berserker rage"

    def use_special(self, target):
        print(f"{self.name} begins to pillage the area and finds some health")
        self.health += 3
        print(f"{self.name} now has {self.health} health")

    def use_buff(self, target):
        print(f"The viking goes into a rage! Def down, Atk up")
        self.strength += 3
        self.defense -= 1

