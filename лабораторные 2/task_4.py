money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month_count = 0
current_balance = money_capital

while current_balance >= 0:
    month_count += 1
    current_balance -= spend  # Платежи за месяц
    if current_balance >= 0:
        current_balance += salary  # Добавляем зарплату
    else:
        break
    spend *= (1 + increase)  # Повышаем расходы согласно росту цен

print("Количество месяцев, которое можно протянуть без долгов:", month_count)
