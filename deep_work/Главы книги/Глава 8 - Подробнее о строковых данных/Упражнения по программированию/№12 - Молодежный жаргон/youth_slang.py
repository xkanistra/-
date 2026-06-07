# Программа преобразует текст в молодежный жаргон

def main():
    text = user_input()
    words_list = add_list(text)
    slang_text = get_slang_text(words_list)
    print(slang_text)

    
def user_input():
    text = input('Введите текст: ')
    return text


def add_list(text):
    word_list = text.split()
    return word_list


def get_slang_text(words_list):
    slang = []
    for group in words_list:
        if group[1:].isupper():
            slang.append(group[1:] + group[0] + 'КИ')               # <- надежнее срез чем lstrip(символ), т.к если будет повтор значения, например АААА, то все АААА будут удалены
        else:
            slang.append(group[1:] + group[0].lower() + 'ки')

    return ' '.join(slang)

if __name__ == '__main__':
    main()