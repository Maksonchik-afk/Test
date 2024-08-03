lst1 = [0, 67, 0, 0, 3, 49]

zero_count = lst1.count(0)
none_zero = lst1[:]

while 0 in none_zero:
    none_zero.remove(0)

lst2 = none_zero + [0] * zero_count
print(lst2)
