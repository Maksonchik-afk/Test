lst = [1]
print('до: ', lst)

if len(lst) > 1:
    x = lst.pop()
    lst.insert(0, x)
    print('після: ', lst)

else:
    print('після:', lst)
