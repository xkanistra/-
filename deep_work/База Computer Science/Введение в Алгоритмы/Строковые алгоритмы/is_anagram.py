# Алгоритм определения анаграм
# Сложность O(n logn)
def main():
    str1 = 'оЛо'
    str2 = 'лоо'    
    anagram = is_anagram(str1, str2)
    print(anagram)

# Определение функции
def is_anagram(s1, s2):
    # s1, s2 убираем лишние пробелы и приводим к нижнему регистру
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    # Сравниваем отсортированные строки, если они равны -> Анаграма, если нет -> не Анаграма
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


if __name__ == '__main__':
    main()