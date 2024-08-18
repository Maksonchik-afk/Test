import string
entered_letters = input('Введіть дві літери через дефіс: ')

start = entered_letters[0]
end = entered_letters[2]

first_index = string.ascii_letters.index(start)
last_index = string.ascii_letters.index(end)

result = string.ascii_letters[first_index:last_index + 1]

print(result)
