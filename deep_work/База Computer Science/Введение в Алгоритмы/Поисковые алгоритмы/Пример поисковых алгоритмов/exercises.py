# Бинарный поиск слов в алфавитном порядке
from bisect import bisect_left

def main():
    word_list = ['А', 'Г', 'Б', 'Д', 'Е', 'В']
    word_list.sort()
    word = input('Введите букву для поиска: ')
    search = binary_search(word_list, word)
    if search == True:
        print('Есть в списке')
    else:
        print(f'Нет в списке')
def binary_search(word_list, word): 
    index = bisect_left(word_list, word)
    if index < len(word_list) and word_list[index] == word:
        return True
    return False

if __name__ == '__main__':
    main()