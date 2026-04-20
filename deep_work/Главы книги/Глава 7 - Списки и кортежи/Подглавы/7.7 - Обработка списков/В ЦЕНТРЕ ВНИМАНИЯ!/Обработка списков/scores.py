# Получает оценки учеников и сохр их в списке

def get_scores():
    # Список
    test_scores = []

    again = 'д'
    total = 0
    while again == 'д' or again == 'Д':
        total += 1
        scores = float(input(f'Введите {total} оценку '))
        
        test_scores.append(scores)

        again = input(f'Желаете продолжить? (д/Д - Да): ')
        print()

    return test_scores

if __name__ == '__main__':
    get_scores()