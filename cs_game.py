from clash import Clash
from warrior import Warrior
from warrior import Ogre
from warrior import Goblin
from warrior import Dragon
import random


class Game:
    def __init__(self, player1_id, player2_id):
        self.player1 = player1
        self.player2 = player2
        self.player1_id = player1_id
        self.player2_id = player2_id

    def intro(self):
        print("the  C O C K Y   S T R O L L E R \n\
\n\
Here is a small intro. \n\
You are a daring vagabond. You wade through the woods coming into sudden clashes and covering your name "
              "with glory or shame.\n")
        # player1_id = 0
        # player2_id = 0
        # self.choose_your_destiny()
        # self.select_player1(player1_id)
        # self.select_player2(player2_id)
        start_game = Clash(self.player1, self.player2)
        return start_game.start_clash()

    def choose_your_destiny(self):
        print("Select your character: \n"
              "1 - Knight \n"
              "2 - Ogre \n"
              "3 - Goblin \n"
              "4 - Dragon (you bloody cheater!)")
        while True:
            try:
                player_id = int(input())
                print(type(player_id), player_id)
                if player_id in range(1, 5):
                    print(f"You chose the {self.player1.name}'s way.")
                    # self.player1 = Warrior(self.player1.player_id)        # Херня какая-то
                    return player_id
                else:
                    print("Choose your destiny (1 to 4):")
            except ValueError:
                print("Choose your destiny (1 to 4):")
            finally:
                pass
'''
    def select_player1(self, player1_id):       # сделать в цикле; относить к классу (или экземпляру?) по id
        if player1_id == 1:
            self.player1 = Warrior(self.player1.name)
        elif player1_id == 2:
            self.player1 = Ogre(self.player1.name)
        elif player1_id == 3:
            self.player1 = Goblin(self.player1.name)
        elif player1_id == 4:
            self.player1 = Dragon(self.player1.name)
        return self.player1
'''

"""
    def select_player2(self, player2_id):
        player2_id = random.randint(1, 4)
        for i in range(1, 5):
            self.player2 = Warrior(player2_id)      # привязать выбор класса к player2_id
        return self.player2
"""


if __name__ == '__main__':
    player1 = Warrior()
    player2 = Warrior()

    play = Game(player1, player2)
    play.intro()


