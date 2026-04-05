# Структуры данных (dataclass)
from dataclasses import dataclass

@dataclass
class ShiftRecord:
    # Модель одной рабочей смены. Все поля типизированны для подсказок IDE и будущей БД

    date: str               # Дата
    accepted_picks: int     # Принято пиков
    issued_picks: int       # Выдано пиков
    pick_income: float      # Доход только с пиков
    shift_income: float     # Фикс за смену (с учетом двойной оплаты)
    gross_salary: float     # Итого до вычета налогов
    net_salary: float       # Итого после вычета налогов

    @property
    def total_picks(self) -> int:
        # Вычисляемое свойство не хранящееся в БД, считается в процессе
        return self.accepted_picks + self.issued_picks