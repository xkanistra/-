# Програма выводит данные о курсе

def main():
    # Все что переведено в комментарии было в старой версии, но я решил для наглядности код оставить в виде комментариев 
    #course_tuple = ('CS101', 'CS102', 'CS103', 'NT110', 'CM241') 
    room_number, teacher, time = get_dict()
    #inf_of_course = get_course_information(room_number, teacher, time, course_tuple)
    inf_of_course = get_course_information(room_number, teacher, time)


def get_dict():
    room_number = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755,
                   'NT110': 1244, 'CM241': 1411}
    teacher = {'CS101': 'Хайнс', 'CS102': 'Альвадор', 'CS103': 'Рич',
                   'NT110': 'Берк', 'CM241': 'Ли'}
    time = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00',
                   'NT110': '11:00', 'CM241': '13:00'}
    return room_number, teacher, time


# def get_course_information(room_number, teacher, time, course):
#     count = 0
#     print('~' * 5, 'Номера курсов', '~' * 5)
#     for crs in course:
#         count += 1
#         print(f'{count}. {crs}')

#     again = 'д'
#     while again.lower() == 'д':
#         try:
#             choice = int(input('Выберите ваш курс: '))
#             if choice == 1:
#                 print(f'Номер аудитории: {room_number[course[0]]}\n'
#                     f'Преподаватель: {teacher[course[0]]}\n'
#                     f'Время: {time[course[0]]}')
#                 again = input('Желаете узнать еще информацию? (д/н) ')

#             elif choice == 2:
#                 print(f'Номер аудитории: {room_number[course[1]]}\n'
#                     f'Преподаватель: {teacher[course[1]]}\n'
#                     f'Время: {time[course[1]]}')
#                 again = input('Желаете узнать еще информацию? (д/н) ')

#             elif choice == 3:
#                 print(f'Номер аудитории: {room_number[course[2]]}\n'
#                     f'Преподаватель: {teacher[course[2]]}\n'
#                     f'Время: {time[course[2]]}')
#                 again = input('Желаете узнать еще информацию? (д/н) ')    

#             elif choice == 4:
#                 print(f'Номер аудитории: {room_number[course[3]]}\n'
#                     f'Преподаватель: {teacher[course[3]]}\n'
#                     f'Время: {time[course[3]]}')
#                 again = input('Желаете узнать еще информацию? (д/н) ')
#             elif choice == 5:
#                 print(f'Номер аудитории: {room_number[course[4]]}\n'
#                     f'Преподаватель: {teacher[course[4]]}\n'
#                     f'Время: {time[course[4]]}')
#                 again = input('Желаете узнать еще информацию? (д/н) ')
            
#         except ValueError:
#             print('Разрешен ввод только чисел!')


def get_course_information(room_number, teacher, time):
    # Позволяет нам не создавать в main отдельный список, уменьшает объем кода
    course = list(room_number.keys())
    count = 0
    print('~' * 5, 'Номера курсов', '~' * 5)
    for crs in course:
        count += 1
        print(f'{count}. {crs}')

    again = 'д'
    while again.lower() == 'д':
        try:    
            choice = int(input('Выберите ваш курс: '))
            
            # Условие позволяет сократить код убрав if-elif и подходит под расшерение, если появятся другие курсы
            if 1 <= choice <= len(course):
                # Получаем ключ курса, для этого по индексу присваиваем строковое значение номера курса переменной
                course_key = course[choice - 1] 
                print(f'Номер аудитории: {room_number[course_key]}\n'
                    f'Преподаватель: {teacher[course_key]}\n'
                    f'Время: {time[course_key]}')
                again = input('Желаете узнать еще информацию? (д/н) ')
            else:
                print(f'Вы ввели несуществующий номер курса, \nпожалуйста выберите один из доступных курсов введя:\n'
                      f'1 - {len(course)}')
        
        except ValueError:
            print('Разрешен ввод только чисел!')

if __name__ == "__main__":
    main()