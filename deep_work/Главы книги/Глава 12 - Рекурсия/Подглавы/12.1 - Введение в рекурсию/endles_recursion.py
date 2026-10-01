# Программа демонстрирует рекурсивную функцию

def main():
    message()

def message():
    print('Это рекурсивная функция')
    message()

if __name__ == '__main__':
    main()