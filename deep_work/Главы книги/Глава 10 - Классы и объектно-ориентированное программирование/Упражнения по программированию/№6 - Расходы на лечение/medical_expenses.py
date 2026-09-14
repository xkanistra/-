# Программа выводит информацию о пациенте и пройденных процедурах


import patient
import procedure
import logging


SAVE_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№6 - Расходы на лечение/inf_file.txt'
LOGGER_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№6 - Расходы на лечение/app.log'


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename=LOGGER_FILE,
    filemode='a' 
)


def main():
    logging.info('Программа запущенна.')
    again = 'д'
    procedure_objects = []
    patient_objects = []

    logging.info('Получаем данные о пациенте')
    full_name, full_adress, mobile_number, emergency_contact = get_patient_inf()

    logging.debug('Начало цикла while.')
    while again.lower() == 'д':
        procedure, date, medic, cost = get_procedure_information()
        procedure_inf_obj, patient_inf_objects = add_inforamtion(procedure, date, medic, cost, full_name, full_adress, mobile_number, emergency_contact)
        procedure_objects.append(procedure_inf_obj)
        patient_objects.append(patient_inf_objects)
        again = input('Желаете продолжить ввод? (д/н): ')

    print(patient_objects)
    logging.debug('Начало цикла for.')
    for obj in procedure_objects:
        print(obj)

    logging.info('Цикл упешно вывел данные объектов класса.')
    logging.info('Программа завершенна.')


# Функция для ввода данных процедур
def get_procedure_information():
    logging.info('Функция get_procedure_information() успешно запущенна.')
    try:
        procedure = input('Введите название процедуры: ')
        date = input('Введите дата процедуры: ')
        medic = input('Введите имя врача, выполняющего процедуру: ')
        cost = float(input('Введите стоимость услуги: '))
        logging.info('Успешный ввод данных.')
        return procedure, date, medic, cost
    except ValueError:
        logging.error('Пользователь совершил неверный формат ввода.')
        print('Введите корректный возраст в числах.')
    except TypeError:
        logging.error('Пользователь совершил неверный формат ввода(запятая вместо точки).')
        print('Введите цену используя "," а не точку.')


# Функция для ввода данных пациентов
def get_patient_inf():
    logging.info('Функция get_patient_inf() успешно запущенна.')
    try:
        full_name = input('Введите ФИО: ')
        full_adress = input('Введите полный адресс: ')
        mobile_number = input('Введите телефонный номер: ')
        emergency_contact = input('Введите контакты доверенного лица: ')
        logging.info('Успешный ввод данных пацинта.')
        return full_name, full_adress, mobile_number, emergency_contact
    except ValueError:
        logging.error('Пользователь совершил неверный формат ввода.')
        print('Введите корректный возраст в числах.')


# Функция создает объекты класса и возвращает их значения
def add_inforamtion(proced, date, medic, cost, full_name, full_adress, mobile_number, emergency_contact):
    logging.info('Функция add_inforamtion() успешно запущенна.')
    proced_obj = procedure.Procedure(proced, date, medic, cost)
    logging.info('Данные успешно переданы в функцию save_inf().')
    patient_obj = patient.Patient(full_name, full_adress, mobile_number, emergency_contact)
    save_inf(proced_obj.inf_list(), patient_obj.inf_list())
    return proced_obj, patient_obj


# Функция сохраняет данные введённые пользователем в файле
def save_inf(proced, patient):
    logging.info('Функция save_inf() успешно запущенна.')
    with open(SAVE_FILE, 'a', encoding='utf-8') as save_file:
        save_file.write(f'{patient}\n')
        save_file.write(f'{proced}\n')
        logging.info('Данные сохранены успешно\n')


if __name__ == '__main__':
    main()