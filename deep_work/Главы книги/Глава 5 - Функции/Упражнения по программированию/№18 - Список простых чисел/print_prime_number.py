# Программа показывает все простые числа от 1 до 100
import is_prime

def main():
    for i in range(1, 101):
        if is_prime.get_prime(i) == True:
            print(i)
        else:
            None

main()
