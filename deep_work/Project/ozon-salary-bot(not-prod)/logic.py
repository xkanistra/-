# Бизнес-логика (расчеты, налоги)
from config import PICK_RATE, SHIFT_RATE, TAX_RATE, FSZN_RATE, TAX_FREE_LIMIT, TAX_FREE_COEF

def calculate_shift_income(accepted: int, issued: int, is_double: bool) -> tuple[float, float, float]:
    # Возвращает (доход с пиков, доход за смену, до вычета налогов)
    picks_income = (accepted + issued) * PICK_RATE
    shift_income = SHIFT_RATE * 2 if is_double else SHIFT_RATE
    return picks_income, shift_income, picks_income + shift_income

def calculate_net_salary(gross: float) -> float:
    # Расчет ЗП после налогов (адаптированно под РБ/СНГ)
    fszn = gross * FSZN_RATE
    taxable = max(0, gross - TAX_FREE_COEF) if gross < TAX_FREE_LIMIT else gross
    tax = taxable * TAX_RATE
    return round(gross - fszn - tax, 2)