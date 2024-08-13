import string
import keyword

input_str = input('Введіть змінну: ')

if input_str[0].isdigit():
    print(False)
else:
    if any(i.isupper() for i in input_str):
        print(False)
    else:
        if any(i in string.punctuation.replace('_', '') for i in input_str):
            print(False)
        else:
            if input_str.count('_') > 1:
                print(False)
            else:
                if input_str in keyword.kwlist:
                    print(False)
                else:
                    print(True)
