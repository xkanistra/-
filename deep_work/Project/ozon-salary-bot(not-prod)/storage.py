# Работа с данными (TXT → потом SQLite/Google Sheets)

import csv
from config import HISTORY_FILE
from models import ShiftRecord

# Абстрактный слой работы с данными. Легко заменить на SQLite/Google Sheets
class SalaryStorage:
    # Метод класса __init__, при создании класса проверяет, существует ли файл HISTORY_FILE, 
    # если нет вызывает метод _create_file() для создания файла, 
    # взаимодействует с HISTORY_FILE сформированный в DATA_DIR / 'salary_history.csv' (config.py)  
    def __init__(self):
        if not HISTORY_FILE.exists():
            self._create_file()

    # Создает CSV-файл в кодировке UTF-8, задает разделить полей | (вместо ,)
    # записывает заголовки столбцов в writer.writerow([....)]
    def _create_file(self):
        with open(HISTORY_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['Дата', 'Принято', 'Выдано', 'За пики', 'За смену', 'До налогов', 'После налогов' ])
    
    # Добавляет новую запись в конец файла, форматирует число :.2f, 
    # сохраняет данные из объекта ShiftRecord и рассчитанную чистую ЗП net_salary
    def save(self, record: ShiftRecord, net_salary: float):
        with open(HISTORY_FILE, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow([
                record.date, record.accepted_picks, record.issued_picks,
                f'{record.pick_income:.2f}', f'{record.shift_income:.2f}',
                f'{record.gross_salary:.2f}', f'{record.net_salary:.2f}' 
            ])

    # Читает файл и преобразует каждую строку в словарь (ключ — название столбца),
    # возвращает последние limit записей (по умолчанию — 10),
    # обрабатывает ошибку FileNotFoundError, если файл отсутствует 
    def get_history(self, limit: int = 10) -> list[dict]:
        # Читает послдение N записей
        records = []
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='|')
                for row in list(reader)[-limit:]:
                    records.append(row)
        except FileNotFoundError:
            pass
        return records
    
    # Суммирует значения из столбца gross для записей, 
    # где месяц в поле date совпадает с month_num.
    # Предполагает, что дата хранится в формате DD.MM.YYYY (разделитель — точка)
    def get_month_total(self, month_num: str) -> float:
        # Сумма gross(до вычета налогов) за конкретный месяц
        total = 0.0
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='|')
                for row in reader:
                    if row['date'].split('.')[1] == month_num:
                        total += float(row['gross'])
        except (FileNotFoundError, ValueError, IndexError):
            pass
        return total