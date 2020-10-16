from clash import Clash
from warrior import Warrior


class Game(Clash, Warrior):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)

    def intro(self):
        print("the  C O C K Y   S T R O L L E R \n\
\n\
Here is a small intro. \n\
You are a daring vagabond. You wade through the woods coming into sudden clashes and covering your name "
              "with glory or shame.\n")
        Clash.start(self)


if __name__ == '__main__':
    player1 = Warrior('Knight')
    player2 = Warrior('Ogre')

    play = Game(player1, player2)
    play.intro()


