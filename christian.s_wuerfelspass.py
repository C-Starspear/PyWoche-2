import random

counter = 0

max_wuerfe = 30

while counter < max_wuerfe:

    zahl = random.randint(1, 6)
    
    counter += 1

    print(f"Wurf {counter}: {zahl}")



