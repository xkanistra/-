import is_prime

def main():
    num1 = int(input('Введите число: '))
    result = is_prime.get_prime(num1)
    if result == True:
        print('Число простое')
    else:
        print('Число не простое')

main()