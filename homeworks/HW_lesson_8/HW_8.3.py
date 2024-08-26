def find_unique_value(some_list):
    count_dict = {}
    for num in some_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count == 1:
            return num


res = find_unique_value([2, 3, 3, 3, 5, 5])
print(res)
