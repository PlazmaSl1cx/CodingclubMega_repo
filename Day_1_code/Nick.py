import random

# placeholder value
dice1 = 1
dice2 = 0
dice3 = 2
dice4 = 3
dice5 = 4

counter = 0
while dice1 != dice2 or dice1 != dice3 or dice1 != dice4 or dice1 != dice5:
    counter += 1

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    dice5 = random.randint(1,6)

    print(dice1, dice2, dice3, dice4, dice5)

print("Rolled the same dice after", counter)
