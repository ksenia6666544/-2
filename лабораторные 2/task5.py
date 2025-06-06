import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10   # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Расчёт подушки безопасности
money_capital = 0

for i in range(months):
    money_capital += spend - salary
    spend *= (1 + increase)

# Округляем всегда вверх
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(math.ceil(money_capital)))

