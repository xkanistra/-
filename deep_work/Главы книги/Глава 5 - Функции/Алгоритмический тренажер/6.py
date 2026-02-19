# Написать функцию которая присваивает случайное число от 1 до 100 переменной radn

import random

def main():
    my_rand()

def my_rand():
    rand = random.randint(1, 100)
    print(rand)

main()