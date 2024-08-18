seconds = int(input('Введіть кількість секунд, від 0 до 8640000: '))

if 0 <= seconds <= 8640000:
    days = seconds // 86400
    seconds %= 86400

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    hours_1 = str(hours).zfill(2)
    minutes_1 = str(minutes).zfill(2)
    seconds_1 = str(seconds).zfill(2)

    if days % 10 == 1 and days % 100 != 11:
        day_str = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_str = "дні"
    else:
        day_str = "днів"

    result = f'{days} {day_str} {hours_1}:{minutes_1}:{seconds_1}'

    print(result)
else:
    print('Невірне значення')
