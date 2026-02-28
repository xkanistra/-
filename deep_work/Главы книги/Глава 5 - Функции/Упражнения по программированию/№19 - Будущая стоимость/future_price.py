# Программа расчитывает сложный процент от суммы денег

MOUNTH = 12

def main():
    year_interest_rate = float(input('Введите годовую процентную ставку: '))
    mounth_interest_rate = get_mounth_rate(year_interest_rate)
    amount_deposit = float(input('Введите текущую сумму на счете: '))
    mounth = int(input('Введите кол-во месяцев в течении которых будут лежать деньги на счету: '))
    total_price = future_price(mounth_interest_rate, amount_deposit, mounth)
    result = total_price - amount_deposit
    print(f'Начальная сумма на счете: {amount_deposit:,.2f} BYN\n'
          f'Доход за {mounth} месяцев: {result:,.2f} BYN\n'
          f'К концу срока депозита останется: {total_price:,.2f} BYN')


def get_mounth_rate(year_interest_rate):
    return (year_interest_rate / MOUNTH) / 100

def future_price(rate, deposit, mounth):
    total = deposit * ((1 + rate) ** mounth)
    return total

main()