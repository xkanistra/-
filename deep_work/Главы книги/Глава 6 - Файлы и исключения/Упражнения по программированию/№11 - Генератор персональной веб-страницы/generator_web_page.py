# Программа генерирует веб страницу HTML

def main():
    name = input('Введите свое имя: ')
    descr = input('Опишите себя: ')

    # Создать файл (шаг 1) 
    html_file = open('my_page.html', 'w')

    # Работа с файлом(шаг 2)
    # Запись HTML разметки
    write_html(html_file, name, descr)

    # Закрыть файл(шаг 3)
    html_file.close()

# В этой функции происходит создание и запись html файла,
# она вызывает другие функции
def write_html(html_file, name, descr):
    # Записать HTML разметку страницы

    # Записать тег <html>
    html_file.write('<html>\n')

    # Запись <head>
    write_head(html_file)

    # Запись <body>
    write_body(html_file, name, descr)

    # Записать тег
    html_file.write('</html\n')

def write_head(html_file):
    # Запись заголовка
    html_file.write('<head>\n')
    html_file.write('<title>Моя персональная веб-страница</title>\n')
    html_file.write('<head>\n')

def write_body(html_file, name, descr):
    # Запись тела страницы
    html_file.write('<body>\n')
    html_file.write('<\t<center>\n')
    html_file.write('\t\t<h1>')
    html_file.write(name)
    html_file.write('\t\t</h1>\n')
    html_file.write('\t<center>\n')
    html_file.write('\t<hr />\n')
    html_file.write(descr)
    html_file.write('\n\t<hr />\n')
    html_file.write('\t</body>\n')

if __name__ == '__main__':
    main()  