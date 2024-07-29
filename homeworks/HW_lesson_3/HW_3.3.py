lst = [1, 2, 3, 4, 5]

result = []

if len(lst) == 0:
    result = [[], []]
else:
    middle = len(lst) // 2
    if len(lst) % 2 != 0:
        middle += 1
    result = [lst[:middle], lst[middle:]]
print(result)
