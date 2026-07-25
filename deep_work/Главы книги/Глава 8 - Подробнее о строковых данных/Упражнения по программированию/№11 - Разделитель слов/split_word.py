# Программа принимает текст и потом возвращает его разделенным и с верными регистрами

def main():
    text = user_input()
    split_text = get_split(text)
    print(split_text[0].upper() + split_text[1:])

def user_input():
    text = input('Введите текст: ')
    return text


def get_split(text):
    new_text = ''
    for ch in text:     
        if ch.isupper():    # <- Тут была ошибка, писал в условии вместо метода проверки .isupper() метод модификации .upper() 
            new_text += ' ' + ch.lower()
        else:
            new_text += ch

    return new_text.strip()


if __name__ == '__main__':
    main()