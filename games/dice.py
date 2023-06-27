import random


def roll_dice():
    return random.randint(1, 6)


# Simulate rolling the dice 5 times
for _ in range(5):
    result = roll_dice()
    print("Dice rolled:", result)
