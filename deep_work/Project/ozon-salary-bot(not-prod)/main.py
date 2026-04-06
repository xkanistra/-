# Точка входа

from config import *
from models import ShiftRecord
from logic import calculate_net_salary, calculate_shift_income
from storage import SalaryStorage
from ui_console import ask_int, ask_yes_no
from datetime import datetime

def main():
    storage =SalaryStorage()
    print("🚀 Калькулятор ЗП Ozon запущен")

    while True:
        print('\n1. Добавить смену  2. История  3. Итого за месяц  4. Выход')
        choice = ask_int('Выбор: ')

        if choice == 1:
            day = ask_int('День (1-31):  ')
            month = ask_int('Месяц (1-12): ')
            # Берём текущий год
            current_year = datetime.now().year
            date_str = f"{day:02d}.{month:02d}.{current_year}"

            accepted = ask_int('Принято пиков: ')
            issued = ask_int('Выдано пиков: ')
            is_double = ask_yes_no('Двойная смена? (1/2): ')

            pick_inc, shift_inc, gross = calculate_shift_income(accepted, issued, is_double)
            net = calculate_net_salary(gross)

            record = ShiftRecord(
                date=date_str,
                accepted_picks=accepted,
                issued_picks=issued,
                pick_income=pick_inc,
                shift_income=shift_inc,
                gross_salary=gross,
                net_salary=net
            )
            storage.save(record, net)
            print(f"✅ Сохранено. Gross: {gross:.2f} | Net: {net:.2f} BYN")
        
        elif choice == 2:
            for row in storage.get_history(5):
                 print(f"📅 {row['Дата']} | До налогов: {row['До налогов']} | После налогов: {row['После налогов']}")
        elif choice == 3:
            m = input("Месяц (01-12): ").zfill(2)
            total = storage.get_month_total(m)
            print(f"💰 Итого за {m}.2026: {total:.2f} BYN (до вычета)")

        elif choice == 4:
            print("👋 До связи!")
            break

if __name__ == "__main__":
    main()