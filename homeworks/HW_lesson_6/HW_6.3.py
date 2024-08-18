num = int(input('Введіть число: '))

while num > 9:
    result = 1
    str_num = str(num)
    for digit in str_num:
        result *= int(digit)

    num = result
print(num)
