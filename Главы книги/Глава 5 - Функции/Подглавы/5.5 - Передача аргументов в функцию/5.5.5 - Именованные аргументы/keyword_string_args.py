# Программа демонстрирует передачу в функцию
# двух строковых значений в качестве именованных аргументов.

def main():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Ваше имя в обратном порядке')
    reverse_name(first = first_name, last = last_name)

def reverse_name(last, first):
    print(last, first)

main()