import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
chance = random.randint(0, 1)
if chance == 1:
    print("Heads")
else:
    print("Tails")