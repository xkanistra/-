# Пример линейного поиска
def main():
    a_list = [1, 52, 66, 33, 69, 51, 55, 420, 52, 30]
    n = 51
    search = linear_search(a_list, n)
    print(search)
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False
    
    

if __name__ == '__main__':
    main()