# Демонстрация лексемизации строковых литералов

def main():
    # Строковые литералты подлежащие лексемизации
    str1 = 'one two three four'
    str2 = '10:20:30:40'
    str3 = 'a/b/c/d/e/f'

    # Вывести на экран лексемы в каждом строк литерале
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')

    # Функция display_tokens выводит на экран лексемы
    # находящие в строковом литерале
    # Параметр data является строковым литералом, подлежащим лексимизации
    # а параметр delimeter - разделителем
def display_tokens(data, delimeter):
    tokens = data.split(delimeter)
    for item in tokens:
        print(f'Лексема: {item}')

if __name__ == '__main__':
    main()