# Вычисляет сумму значений в списке

def get_total(scores):
    total = 0.0

    for num in scores:
        total += num

    return total

if __name__ == '__main__':
    get_total()