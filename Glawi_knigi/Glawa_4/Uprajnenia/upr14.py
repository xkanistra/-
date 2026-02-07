# Рисование звездочек

BASE_SIZE = 7 

for r in range(BASE_SIZE, 0, -1): 
    for c in range(r):
        print("*", end="")
    print()
