# Рисуем пирамиду из #

NUM_STEPS = 6

for r in range(NUM_STEPS):
    print('#', end = '')
    for c in range(r):
        print(" ", end="")
    print("#")
    