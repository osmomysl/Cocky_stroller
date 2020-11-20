import random
from datetime import datetime
random.seed(datetime.now())


class Warrior:
    def __init__(self, name, health, strength, agility, luck):
        self.name = name
        self.health = health
        self.hp = self.health
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.chance = (self.agility + self.luck) / 2
        self.min = (self.luck / 100) * self.strength
        self.max = self.strength

    def make_damage(self):
        hit = random.randint(self.min, self.max)
        return hit

    def take_damage(self, hit):
        if not self.dodge():
            self.hp -= hit
            print(f"The {self.name} got hit for {hit} HP.")
        print('{:11}'.format(self.name), "\u2764 " + self.hp * '|', self.hp if self.hp > 0 else 0)
        return self.hp

    def dodge(self):    # шанс увернуться от удара
        fate = random.randint(0, 100)
        if self.chance > fate:
            # print('DODGE! {} chance, {} fate'.format(self.chance, self.fate))
            print(f"The {self.name} dodged a punch. His opponent missed.")
            return True
        else:
            # print('FAILURE! {} chance, {} fate'.format(self.chance, self.fate))
            return False

    def is_alive(self):
        return self.hp > 0
