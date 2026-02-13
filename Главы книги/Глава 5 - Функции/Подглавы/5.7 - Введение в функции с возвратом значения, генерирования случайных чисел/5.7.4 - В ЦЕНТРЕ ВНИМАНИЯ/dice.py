# Эта программа имитирует бросание кубиков.
import random

# Константы для мин. и макс. случайных чисел
MIN = 1
MAX = 6

def main():
    # Создать переменную для управления циклом 
    again = 'д'

    # Имитировать бросание кубиков
    while again == 'Д' or again == 'д':
        print('Бросаем кубики...')
        print('Значение граней:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Сделать еще один бросок кубиков?
        again = input('Бросить кубики еще раз? (д = да): ')

main()