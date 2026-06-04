# Программа выводи на экран самый часто появляющийся символ


from bisect import bisect_left, bisect_right


def main():
    text = input_text()
    list_item = add_list(text)
    char, count = binary_search(list_item, text)
    print(f'Самый частый символ: "{char}" появляется {count} раз')


def input_text():
    text = input('Введите текст: ')
    return text


def add_list(text):
    list1 = []
    for ch in text:
        list1.append(ch)
    list1.sort()
    return list1


def binary_search(list_item, text):
    max_count = 0
    best_ch = ''
    for ch in set(text):
        left_index = bisect_left(list_item, ch)
        right_index = bisect_right(list_item, ch)
        count = right_index - left_index
        if count > max_count:
            max_count = count
            best_ch = ch
    return best_ch, max_count
    

if __name__ == '__main__':
    main()