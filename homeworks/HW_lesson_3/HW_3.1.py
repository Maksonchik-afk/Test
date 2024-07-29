print('Вас вітає найпростіший калькулятор')

number_1 = float(input('Введіть перше число: '))
math_operation = input('Введіть математичну дію, / , *, -, + : ')
number_2 = float(input('Введіть друге число: '))

result = None

if math_operation == '+':
    result = number_1 + number_2
    print(result)

elif math_operation == '-':
    result = number_1 - number_2
    print(result)

if math_operation == '*':
    result = number_1 * number_2
    print(result)

elif math_operation == '/':
    if number_2 != 0:
        result = number_1 / number_2
        print(result)
    else:
        print('На нуль ділити не можна!!!')
