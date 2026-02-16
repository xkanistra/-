# Программа возвращает несколько переменных

def main():
    # Во время вызова инструкции get_name слева от = следует исп. две переменных,
    # вот пример:  
    first_name, last_name = get_name()
    print(first_name, last_name)
    
def get_name():
    # Получить имя и фамилию пользователя
    first = input('Введите свое имя: ')
    last = input('Введите свою фамилию: ')

    #Вернуть оба значения
    return last, first

main()