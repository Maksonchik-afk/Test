number = int(input("Введіть п'ятизначне число: "))

thousands = (number % 10)
thousand = (number % 100) // 10
hundred = (number % 1000) // 100
ten = (number % 10000) // 1000
unit = (number // 10000)

reserve_number = thousands * 10000 + thousand * 1000 + hundred * 100 + ten * 10 + unit

print(reserve_number)
