# Алгоритм шифра Цезаря

import string

def main():
    str1 = 'I love Liza four year'
    key = int(input('Введите смещение: '))
    encrypt = cipher(str1, key)
    print(encrypt)

# Функция принимает строку и ключ для смещения
def cipher(a_string, key):
    # Берем англ алфавит в верхнем регистре и нижнем из библиотеки string
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    # Пустое значение которое будет принимать шифр
    encrypt = ''
    # Читаем каждую букву из текста
    for c in a_string:
        # Если есть буква из текста в алфавите в нижнем/верхнем регистре то:
        if c in uppercase:
            # присваиваем переменной new индекс новой, смещенной буквы через формулу
            new = (uppercase.index(c) + key) % 26
            # По индексу добавляем смещенную букву переменной зашифр.текста
            encrypt += uppercase[new]
        # Тоже самое что выше
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        # Если в тексте элементы не являющиеся буквами, то добавляются без изменения
        else:
            encrypt += c
    return encrypt

if __name__ == '__main__':
    main()