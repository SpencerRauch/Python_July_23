from game_classes.fighter import Fighter

class Ninja(Fighter):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength = 14
        self.defense = 0
        self.special = "roundhouse kick"
        self.buff = "intimidate"

    def use_special(self, target):
        print(f'{self.name} issues a roundhouse kick to {target.name}')
        target.defend(20)

    def use_buff(self, target):
        print(f"{self.name} stares down {target.name}")
        target.strength -= 2
        print(f"{target.name} is afraid, attack lowered")

    