def main():
    string = input('Введите текст: ')
    reverse_string(string)

def reverse_string(string):
    reverse_str = string[::-1]
    print(reverse_str)
if __name__ == '__main__':
    main()
