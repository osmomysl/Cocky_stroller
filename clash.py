from warrior_factory import WarriorFactory
import random
from datetime import datetime
random.seed(datetime.now())


class Clash:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.wins = 0
        self.escapes = 0

    def select_opponent(self):
        player_id = random.randint(1, 4)
        self.player2 = WarriorFactory.create_by_id(player_id)
        pass

    def start(self):
        self.player1.hp = self.player1.health   # восстанавливаем здоровье player1
        self.select_opponent()                  # создаём player2
        if self.player2.name == self.player1.name:
            self.player2.name = 'Dark ' + self.player2.name
        self.message_start()
        return self.fight_or_run()

    def fight_or_run(self):
        while True:
            your_choice = input()
            if your_choice.casefold() == 'f':
                if self.escapes == 0:
                    return self.combat()
                else:
                    break
            elif your_choice.casefold() == 'r':
                self.escapes = 0
                self.message_run(1)
                return self.start()
            else:
                self.message_run(2)
                pass

    def combat(self):
        while self.player1.is_alive() and self.player2.is_alive():
            p1_damage = self.player1.make_damage()
            self.player2.take_damage(p1_damage)
            p2_damage = self.player2.make_damage()
            self.player1.take_damage(p2_damage)
            self.checkup()
        else:
            if self.player1.is_alive():
                self.wins += 1
                self.escapes = 0
                self.message_victory()
                return self.start()
            else:
                self.message_failure()
                return self.restart()

    def checkup(self):
        if self.player1.is_alive() and self.player2.is_alive():
            if self.player1.hp / self.player1.health < 0.5 and self.escapes == 0:
                self.escapes += 1
                self.message_checkup()
                return self.fight_or_run()
            elif self.player1.hp / self.player1.health < 0.15 and self.escapes == 1:
                self.escapes += 1
                self.message_checkup()
                return self.fight_or_run()
            else:
                pass

    def restart(self):
        print("\nRestart? (y) / (n)")
        while True:
            restart = input()
            if restart.casefold() == 'y':
                self.wins = 0
                self.escapes = 0
                return self.start()
            elif restart.casefold() == 'n':  # !!!!!!!!!!!!!!!!!!!!!!! сколько раз запущен combat, столько же закрывать restart
                break
            else:
                print('Choose: "yes" (y) or "no" (n)?')
                pass

    def message_start(self):
        print(f"You have faced an enemy: {self.player2.name} ({self.player2.hp} HP) \n"
              f"What are you going to do: fight (f) or run away (r)?")

    @staticmethod
    def message_checkup():
        print("\nYou are wounded and exhausted.\n"
              "Do you want to save your life by leaving the battle (r) or fight to the last breath (f)?")

    @staticmethod
    def message_run(step):
        if step == 1:
            print("You ran away from the enemy. \n"
                  "You're still alive, but you haven't gained any glory.\n")
        elif step == 2:
            print("Make your decision: \u2694 (f) or \U0001F3C3 (r)?")

    def message_victory(self):
        print(f"\n🚩 Congratulations, brave {self.player1.name}! "
              f"You've overcame the {self.player2.name} 🚩\n"
              f"Trophy count: '{self.wins}'.\n")

    def message_failure(self):
        print(f"\n💀 You've been killed.\n"
              f"{'':3}Game over.\n"
              f"{'':3}You achieved '{self.wins}' victories. 💀")
