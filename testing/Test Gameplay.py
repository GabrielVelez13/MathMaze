# The goal is to recieve a question and have a maximum time to complete it.
# The enemy must have some health which each correct answer decreases and each incorrect answer increases
# Similarly the player has a set ammount of health, once they are gone the game is over

from random import randint
class Enemy:
    def __init__(self, health=100, seconds=10):
        self.health = health
        self.time = seconds

    def sum_question(self):
        a = randint(1, 9)
        b = randint(1, 9)
        question = f"What is {a} + {b}?"
        if int(input(question)) == a + b:
            print("Good")
        else:
            print("Bad")

if __name__ == '__main__':
    enemy = Enemy()
    while True:
        enemy.sum_question()