# Программа читает/принимает текст и шифрует его по значениям из словаря


ENCRYPTION_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/Шифруемый текст.txt'
DECRYPTION_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/Дешифруемый текст.txt'

def main():
    # Словарь кодов
    codes = {
    # Буквы верхнего регистра
    'А':'!', 'Б':'№', 'В':'@', 'Г':'#', 'Д':'%', 'Е':':', 'Ё':'?', 'Ж':'*', 'З':'(', 'И':')', 'Й':'-', 'К':'_', 'Л':'+', 'М':'=', 'Н':'^',
    'О':'&', 'П':'**', 'Р':'11', 'С':'2', 'Т':'3', 'У':'14', 'Ф':'24', 'Х':'145', 'Ц':'55', 'Ч':'6-', 'Ш':'77=', 'Щ':'%8', 'Ъ':'%$', 'Ы':'$#', 'Ь':'#@', 'Э':'!@', 'Ю':'!6@', 'Я':'199',
    # Пробел и символы
    ' ':'_/_', ',': ',,', '!': '..', '.': '...', '?': '???',
    # Буквы нижнего регистра
    'а':'#1', 'б': '#2', 'в': '##3', 'г': '##1', 'д': '#5', 'е': '01', 'ё': '110', 'ж': '010', 'з': '142', 'и': '1*-', 'й': '1/2', 'к': '1129', 'л': '98',
    'м': '09', 'н': '78', 'о': '22', 'п': '13', 'р': '44', 'с': '12', 'т': '##21', 'у': '#!!', 'ф': '!!#', 'х': '#4', 'ц': '0', 'ч': '2212', 'ш': '**-**',
    'щ': '**__', 'ъ': '__0', 'ы': '(--)', 'ь': '(00)', 'э': '@@', 'ю': '@!', 'я': '!!@@',
    }

    encryption_file = open_file()
    encryption_text = get_encryption_file(encryption_file, codes)
    save_encryption_file(encryption_text)

    decryption_file = open_decryption_file()
    get_decryption_file(decryption_file, codes)


# Функция читает исходный текст(до шифровки) и измененный текст(после шифровки)
def open_file():
    # Ловим ошибку если имя файла изменится или файла не будет
    try:
        # Пустые списки, чтобы собрать текст без символа переноса строки
        encryption_file = []
        with open(ENCRYPTION_FILE, 'r', encoding='utf-8') as file:
            read_file = file.readlines()
            for group in read_file:
                text = group.rstrip('\n')
                encryption_file.append(text)
            print('Файл успешно прочитан!')
        return encryption_file
        
    except FileNotFoundError:
        print(f'Произошла ошибка чтения.\n Проверьте название файла: \n{ENCRYPTION_FILE}')
        return None, None
    except IOError as e:
        print(f'Ошибка чтения файла: {e}')
        return None, None


# Функция читает измененный текст(после шифровки)
def open_decryption_file():
    # Ловим ошибку если имя файла изменится или файла не будет
    try:
        # Пустые списки, чтобы собрать текст без символа переноса строки
        decryption_file = []
        with open(DECRYPTION_FILE, 'r', encoding='utf-8') as file:
                read_file = file.readlines()
                for group in read_file:
                    text = group.rstrip('\n')
                    decryption_file.append(text)
        return decryption_file
    
    except FileNotFoundError:
        print(f'Произошла ошибка чтения.\n Проверьте название файла: \n{DECRYPTION_FILE}')
        return None, None
    except IOError as e:
        print(f'Ошибка чтения файла: {e}')
        return None, None


# Функция шифрует текст 
def get_encryption_file(file, codes):
    # Пустой список для сбора зашифрованного текста в него
    encryption_list = []
    # Читаем элементы списка
    for line in file:
        # Читаем строки внутри элементов списка
        for char in line:
            # Условие, если значение строки есть в ключе словаря, то добавляем значения ключа
            if char in codes:
                code = codes[char]
                encryption_list.append(code)
                encryption_list.append('|')         # Используем | в качестве разделителя слов, для дальнейшей расшифровки
            else:
                encryption_list.append(char)
    
    return ''.join(encryption_list)                 # Собираем в строку


# Функция сохраняет зашифрованный текст
def save_encryption_file(text):
        # Ловим ошибку если имя файла изменится или файла не будет
        try:
            with open(DECRYPTION_FILE, 'w', encoding='utf-8') as save_file:
                save_file.write(f'{text}\n')
            print('Файл успешно сохранен!')
        except FileNotFoundError:
            print(f'Произошла ошибка сохранения.\n Проверьте название файла: \n{DECRYPTION_FILE}')
            return None, None
        except IOError as e:
            print(f'Ошибка чтения файла: {e}')
            return None, None


# Функция расшифровывает текст и выводит его на экран
def get_decryption_file(file, codes):
    # Реверсивно собираем словарь, ставь на место ключа значение, а на место значения ключ
    reverse_code = {v:k for k, v in codes.items()}
    # Пустой список для сбора расшифрованного текста в него
    decryption_list = []
    # Собираем в строку список который вернулся из def open_file()
    encrypt_text = ''.join(file)
    # Убираем лишний | в конце, чтобы не было лишних символов
    encrypt_text = encrypt_text.rstrip('|')
    # Разбиваем строку по разделителю, чтобы разбить текст на элементы списка по буквенно
    parts = encrypt_text.split('|')
    # Читаем элементы списка циклом
    for part in parts:
        # Если элемент, который стал строкой есть как ключ в словаре, то передаем значение ключа и добавляем в пустой список
        if part in reverse_code:
            char = reverse_code[part]
            decryption_list.append(char)
        else:
            decryption_list.append(part)
    # Вывод расшифрованного текста
    print(''.join(decryption_list))     

if __name__ == '__main__':
    main()