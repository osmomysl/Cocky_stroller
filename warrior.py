import random
from datetime import datetime
random.seed(datetime.now())


class Warrior:
    def __init__(self, name, health=100, strength=40, agility=70, luck=50):
        self.name = name
        self.health = health
        self.hp = self.health
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.chance = (self.agility + self.luck)/2
        self.fate = 1
        self.hit = 1
        self.min = (self.luck/100) * self.strength
        self.max = self.strength

    def make_damage(self):
        hit = random.randint(self.min, self.max)
        # print(f"{self.name} hits {other.name}")
        # print('{} min, {} max, {} hit'.format(self.min, self.max, hit))
        # print("p2 пытается увернуться")
        return hit

    def take_damage(self, hit):
        if not self.dodge():
            self.hp -= hit
            print(f"The {self.name} got hit for {hit} HP.")
        print(f"{self.name} \u2764 ", self.hp * '.')
        return self.hp

    def dodge(self):    # шанс увернуться от удара
        self.fate = random.randint(0, 100)
        if self.chance > self.fate:
            # print('DODGE! {} chance, {} fate'.format(self.chance, self.fate))
            print(f"The {self.name} dodged a punch. The enemy missed.")
            return True
        else:
            # print('FAILURE! {} chance, {} fate'.format(self.chance, self.fate))
            return False

    def is_alive(self):
        return self.hp > 0
