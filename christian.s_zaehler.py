import random


counter = 0


for _ in range(5):

    zahl = random.randint(1, 6)


    counter += 1


    print(f"Wurf {counter}: {zahl}")