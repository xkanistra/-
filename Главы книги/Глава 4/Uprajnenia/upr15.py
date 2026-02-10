# Рисуем пирамиду из #

NUM_STEPS = 6

for r in range(NUM_STEPS):
    print("1", end="")
    for c in range(r):
        print(" ", end="")
    print("#")
