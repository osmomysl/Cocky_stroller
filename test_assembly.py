import random
from datetime import datetime
random.seed(datetime.now())



class Warrior:
    def __init__(self, name, health, player_id):
        self.player_id = player_id
        self.name = name
        self.health = health
        self.min = 10
        self.max = 20

    def make_damage(self):
        hit = random.randint(self.min, self.max)
        return hit

    def take_damage(self, hit):
        return print(f"The {self.name} got hit for {hit} HP.")


Ogre = Warrior('Ogre', 150, 1)
Goblin = Warrior('Goblin', 70, 2)



class Clash:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        # self.wins = 0

    def start_clash(self):
        self.player1 = Warrior(player_id = id1)
        self.player2 = Warrior(player_id = id2)
        print(f"You have faced an enemy: {self.player2.name} ({self.player2.health} HP)")
        return self.combat()

    def combat(self):
        p1_damage = self.player1.make_damage()
        self.player2.take_damage(p1_damage)
        p2_damage = self.player2.make_damage()
        self.player1.take_damage(p2_damage)



class Game:
    def __init__(self, player1, player2,  id1, id2):
        self.player1 = player1
        self.player2 = player2
        self.id1 = id1
        self.id2 = id2

    def intro(self):
        print("the  C O C K Y   S T R O L L E R")
        start_game = Clash(self.player1, self.player2)  # NB!!!!
        return start_game.start_clash()

    def choose_your_destiny(self):
        print("Select your character: \n"
              "1 - Ogre \n"
              "2 - Goblin \n"
              )
        while True:
            try:
                self.id1 = int(input())
                if self.id1 in range(1, 3):
                    self.player1 = Warrior(self.player1.name, self.player1.health, player_id=id1)
                    print(f"You chose the {self.player1.name}'s way.")
                    return print(self.id1)
                else:
                    print("Choose your destiny (1 to 2):")
            except ValueError:
                print("Choose your destiny (1 to 2):")
            finally:
                pass


if __name__ == '__main__':
    player1 = Goblin
    player2 = Goblin
    id1 = 0
    id2 = 0

    igra = Game(player1, player2, id1, id2)
    igra.choose_your_destiny()
