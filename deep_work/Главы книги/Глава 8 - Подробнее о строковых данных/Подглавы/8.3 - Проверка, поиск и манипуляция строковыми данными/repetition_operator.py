# Демонстрация оператора повторения

def main():
    # Напечатать 9 строк увелич по длинне
    for count in range(1, 10):
        print('Z' * count)

    # Напечатать 9 строк, уменьш по длинне
    for count in range(8, 0, -1):
        print('Z' * count)
        
if __name__ == "__main__":
    main()