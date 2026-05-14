def main():
    a_list = [2, 6, 9, 20, 3, 56, 55, 12, 36]
    sort = buble_sort(a_list)
    print(sort)
def buble_sort(a_list):
    list_lenght = len(a_list) - 1
    for i in range(list_lenght):
        for j in range(list_lenght):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list

if __name__ == '__main__':
    main()