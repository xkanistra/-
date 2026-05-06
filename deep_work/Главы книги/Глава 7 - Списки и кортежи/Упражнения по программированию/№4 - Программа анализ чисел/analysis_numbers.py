# Анализатор введенных чисел


def main():
    numbers_list = add_numbers()
    numbers_list.sort()
    total_value, average_num, min_value, max_value = get_total(numbers_list)
    
    print(numbers_list)
    print(
        f"Наименьшее число: {min_value}\n"
        f"Наибольшее число: {max_value}\n"
        f"Сумма чисел: {total_value}\n"
        f"Среднее: {average_num}"
    )


def add_numbers():
    total = 0
    num_list = []
    while total != 20:
        total += 1
        numbers = int(input(f"Введитe {total} число: "))
        num_list.append(numbers)
    return num_list


def get_total(numbers_list):
    total_value = 0
    total = 0

    for item in numbers_list:
        total_value += item
        total += 1

    average_num = total_value / total
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    return total_value, average_num, min_value, max_value


if __name__ == "__main__":
    main()
