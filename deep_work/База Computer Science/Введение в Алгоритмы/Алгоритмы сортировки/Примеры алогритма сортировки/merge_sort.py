# Алгоритм сортировки слиянием
def main():
    a_list = [2, 6, 9, 20, 3, 56, 55, 12, 36]
    print(f'До:\n{a_list}')
    merge_sort(a_list)
    print(f'После:\n{a_list}')

# Определение функции
def merge_sort(a_list):
    # Терминальная ветвь рекурсии, отвечает за начало работы рекурсии
    if len(a_list) > 1:
        # Разбиение списка на малые списки
        mid = len(a_list) // 2
        # Указание переменных для получения нужных элементов списка
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        # Рекурсивный вызов функций с аргументом в виде значений списка
        merge_sort(left_half)
        merge_sort(right_half)

        # Индексы для элементов списка
        left_ind = 0
        right_ind = 0
        alist_ind = 0   
        # Три условия while, они являются циклами слияния, при которых индексы должны быть меньше длинны списков
        while left_ind < len(left_half) and right_ind < len(right_half):
            # Сравнение двух списков(которые получились при разбиении основного списка), и установка элементов в нужном порядке
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_half):
            # Финальная сортировка и слияние двух списков
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1
        
        while right_ind < len(right_half):
            # Финальная сортировка и слияние двух списков
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1
        

if __name__ == '__main__':
    main()