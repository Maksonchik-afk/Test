lst = [0, 1, 7, 2, 4, 8]
if len(lst) > 0:
    x = sum((lst[::2]))
    print(x * lst[-1])
else:
    print(0)
