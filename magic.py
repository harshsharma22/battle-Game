import random
class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.damage = dmg
        self.type = type

    def generate_damage(self):
        low= self.damage - 15
        high = self.damage +15
        return random.randrange(low,high)