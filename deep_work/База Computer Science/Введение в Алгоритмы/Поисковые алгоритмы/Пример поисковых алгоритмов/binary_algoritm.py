# Пример двоичного поиска
def main():
    a_list = [1, 52, 66, 33, 69, 51, 55, 420, 52, 30]
    a_list.sort()
    n = 15
    search = binary_search(a_list, n)
    print(search)

def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

if __name__ == '__main__':
    main()