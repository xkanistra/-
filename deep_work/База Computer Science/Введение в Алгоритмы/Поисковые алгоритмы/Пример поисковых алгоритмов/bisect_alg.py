# Пример использования модуля bisect

from bisect import bisect_left
def main():
    a_list = [1, 52, 66, 33, 69, 51, 55, 420, 52, 30]
    a_list.sort()
    n = 66
    search = binary_search(a_list, n)
    print(search)

def binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False

if __name__ == '__main__':
    main()