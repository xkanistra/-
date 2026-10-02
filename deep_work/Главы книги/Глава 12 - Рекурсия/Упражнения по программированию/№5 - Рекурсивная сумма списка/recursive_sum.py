# Программа находит сумму значений в списке рекурсивно


def main():
    a_list = [10, 22, 30, 15, 16, 85, 86, 12, 25, 99, 10, 11]
    print()
    print(a_list)
    sum_list = a_list.copy()
    rec_list(sum_list)
    print()
    print(sum_list)
    

def rec_list(a_list):
    if len(a_list) == 1:
        print(a_list[0])
    else:
        sum = a_list[0] + a_list[1]
        del a_list[1]
        del a_list[0]
        a_list.insert(0, sum)
        print(a_list)
        rec_list(a_list)

main()
