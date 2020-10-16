from warrior import Warrior


class Clash(Warrior):
    def __init__(self, player1, player2):
        super().__init__(self)
        self.player1 = player1
        self.player2 = player2
        self.wins = 0

    def start(self):
        self.player1 = Warrior(self.player1.name)
        self.player2 = Warrior(self.player2.name)
        print(f"You have faced an enemy: {self.player2.name} ({self.player2.hp} HP) \n\
What are you going to do: fight (f) or run away (r)?")
        while True:
            try:
                your_choice = input()
                if your_choice == 'f':
                    print("\u2694 Clash! \u2694")
                    return self.combat()
                elif your_choice == 'r':
                    print("You ran away from the enemy. \n\
You're still alive, but you haven't gained any glory.")
                    print()
                    return Clash.start(self)
                else:
                    print("Make your decision: \u2694 (f) or \U0001F3C3 (r)?")
            finally:
                pass

    def combat(self):
        while self.player1.is_alive() and self.player2.is_alive():
            p1_damage = self.player1.make_damage()
            self.player2.take_damage(p1_damage)
            p2_damage = self.player2.make_damage()
            self.player1.take_damage(p2_damage)
        else:
            if self.player1.is_alive():
                self.wins += 1
                print(
                    f"\U0001F339 Congratulations, brave {self.player1.name}! "
                    f"You've overwhelmed the {self.player2.name} \U0001F339")
                print()
                Clash.start(self)
            else:
                print(f"\n\
\U0001F480 You've been killed. \n\
   Game over. \n\
   You achieved '{self.wins}' victories. \U0001F480")
                print("\nRestart? (y) / (n)")
                while True:
                    try:
                        restart = input()
                        if restart == 'y':
                            self.wins = 0
                            Clash.start(self)
                        elif restart == 'n':
                            break
                        else:
                            print("Choose yes (y) or no (n)?")
                    finally:
                        pass
