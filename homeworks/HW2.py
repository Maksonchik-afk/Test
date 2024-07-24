number = int(input('Введіть чотирьохзначне число: '))

thousand = (number // 1000)
hundred = (number % 1000) // 100
ten = (number % 100) // 10
unit = (number % 100) % 10

print(thousand)
print(hundred)
print(ten)
print(unit)
