import random
from datetime import datetime
random.seed(datetime.now())

"""
Возможно, нужен декоратор для присвоения id экземплярам или наследуемым классам?
"""

class Warrior:      # the basic class
    def __init__(self, player_id=0, name='Knight', health=100, strength=40, agility=70, luck=50):
        self.player_id = player_id
        self.name = name
        self.health = health
        self.hp = self.health
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.chance = (self.agility + self.luck)/2
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
        print('{:6}'.format(self.name), "\u2764 " + self.hp * '|', self.hp if self.hp > 0 else 0)
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


class Ogre(Warrior):        # strong but clumsy
    def __init__(self, player_id=1, name='Ogre', health=150, strength=80, agility=20, luck=40):
        super().__init__(player_id, name, health, strength, agility, luck)
        self.player_id = player_id


class Goblin(Warrior):      # agile but weak
    def __init__(self, player_id=2, name='Goblin', health=70, strength=30, agility=90, luck=50):
        super().__init__(player_id, name, health, strength, agility, luck)
        self.player_id = player_id


class Dragon(Warrior):      # the killer
    def __init__(self, player_id=3, name='Dragon', health=300, strength=150, agility=10, luck=20):
        super().__init__(player_id, name, health, strength, agility, luck)
        self.player_id = player_id
