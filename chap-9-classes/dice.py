# 9-14, 9-15
import random
class Dice:
    def __init__(self):
        self.sides = 6
        
    def roll_dice(self):
        print(f"{random.randint(1, self.sides)}")

dice = Dice()
for i in range(10):
    dice.roll_dice()
print()
lottery = [1, 23, 3, 'd', 'l', 2, 0, 7, 9, 'k', 'm', 6, 5, 4, 'o']
my_ticket = [1, 3, 'l', 'm']
choices = []
failed = True
times = 0
while(failed):
    times += 1
    for i in range(4):
        c = random.choice(lottery)
        print(c)
        choices.append(c)
    print("Any ticket matching these four numbers of letter wins a prize!")
    if my_ticket == choices:
        failed = False
    choices = []
print(f"Win after {times} times!")
