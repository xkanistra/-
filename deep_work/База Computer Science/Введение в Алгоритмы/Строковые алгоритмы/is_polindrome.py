# Алгоритм поиска полиндрома
# Сложность O(n)
def main():
    str1 = 'оЛо' 
    polidrome = is_polidrome(str1)
    print(polidrome)


def is_polidrome(s1):
    # Сравниваем исходную строку и реверсивную строку
    # [::-1] - делает реверсию строки
    if s1.lower() == s1[::-1].lower():
        return True
    return False

if __name__ == '__main__':
    main()
