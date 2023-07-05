class Fighter:
    def __init__(self):
        self.name = "Generic Name"
        self.health = 100
        self.speed = 10
        self.strength = 10
        self.defense = 3
        self.special = "not implemented"
        self.buff = "not implemented"

    def attack(self, target: "Fighter"):
        print(f"{self.name} is attacking {target.name}")
        target.defend(self.strength)

    def defend(self, amount):
        damage = amount - self.defense
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage and now has {self.health} health")

    def use_special(self):
        raise NotImplementedError
    
    def use_buff(self):
        raise NotImplementedError

    
class Example:
    pass