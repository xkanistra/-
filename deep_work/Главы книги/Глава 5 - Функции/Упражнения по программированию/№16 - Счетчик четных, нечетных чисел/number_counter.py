# Программа посчитывает кол-во четных/нечетных чисел
import random

def main():
    even_total = 0
    even_num = get_even_num(even_total)
    not_even_num = 100 - even_num
    print(f'Четных чисел: {even_num}\nНечетных чисел: {not_even_num}')

def get_even_num(evn_ttl):
    for rand in range(100):
        num = random.randint(1, 100)
        if (num % 2) == 0:
            evn_ttl += 1 
    return evn_ttl 
main() 
