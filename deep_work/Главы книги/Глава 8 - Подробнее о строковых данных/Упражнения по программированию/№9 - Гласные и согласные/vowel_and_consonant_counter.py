# Программа подсчитывает количество гласных и согласных в предложении

VOWELS_TUPLE = ('а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я')
CONSONANTS_TUPLE = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')

def main():
    user_input = usr_input()
    vowels = get_vowels(user_input)
    consonants = get_consonants(user_input)
    print(f'Гласных в предложении: {vowels}\n'
          f'Согласных в предложении: {consonants}')

def usr_input():
    string = input('Введите предложение: ')
    return string


def get_vowels(user_input):
    total = 0   
    for ch in user_input:
        if ch.lower() in VOWELS_TUPLE:
            total += 1

    return total


def get_consonants(user_input):
    total = 0
    for ch in user_input:
        if ch.lower() in CONSONANTS_TUPLE:
            total += 1

    return total


if __name__ == '__main__':
    main()