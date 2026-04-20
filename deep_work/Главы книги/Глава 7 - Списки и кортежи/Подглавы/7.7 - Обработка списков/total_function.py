# Программа демонстрирует применение функций для вычисления
# суммы значений в списке

def main():
    # Список
    numbers = [2, 4, 6, 8, 10]

    # Показать сумму значений списка
    print(f'Сумма состовляет: {get_total(numbers)}')

# Функция принимает аргументом список, и возвращает сумму списка
def get_total(numbers):
    total = 0

    for num in numbers:
        total += num
    
    return total
    
if __name__ == '__main__':
    main()