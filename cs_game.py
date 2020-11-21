from clash import Clash
from warrior_factory import WarriorFactory


class Game:
    def __init__(self):       # (self, player1, player2)
        self.player1 = None
        self.player2 = None

    @staticmethod
    def intro():
        print("the  C O C K Y   S T R O L L E R \n"
              "Here is a small intro. \n"
              "You are a daring vagabond. You wade through the woods coming into sudden clashes and covering your name "
              "with glory or shame.\n\n"
              "Select your character: \n"
              "1 - Knight \n"
              "2 - Ogre \n"
              "3 - Goblin \n"
              "4 - Dragon (you bloody cheater!)")

    def choose_your_destiny(self):
        while True:
            try:
                player_id = int(input())
                if player_id in range(1, 5):
                    self.player1 = WarriorFactory.create_by_id(player_id)
                    print(f"You chose the {self.player1.name}'s way.\n")
                    break
                else:
                    print("Choose your destiny (1 to 4):")
                    pass
            except ValueError:
                print("Choose your destiny (1 to 4):")
            finally:
                pass

    def start(self):
        Game.intro()
        self.choose_your_destiny()
        clash = Clash(self.player1, self.player2)
        clash.start()


if __name__ == '__main__':
    game = Game()
    game.start()


