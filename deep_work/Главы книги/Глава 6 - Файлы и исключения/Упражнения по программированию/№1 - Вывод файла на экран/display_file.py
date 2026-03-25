# Программа выводит содержимое файла на экран
def main():
    num_file = open('number_list.txt', 'r')

    line = num_file.read()
    print(line)
    
    num_file.close()
if __name__ == '__main__':
    main()