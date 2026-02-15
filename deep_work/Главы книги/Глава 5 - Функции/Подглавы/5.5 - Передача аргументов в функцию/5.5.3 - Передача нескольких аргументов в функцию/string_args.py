# Программа демонстрирует передачу в качестве аргументов
# строковые значения.

def main():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Ваше имя в обратном порядке')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

main()