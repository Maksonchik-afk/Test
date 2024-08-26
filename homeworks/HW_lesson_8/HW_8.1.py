def add_one(some_list):
    join_type = ''.join([str(x) for x in some_list])
    number_type = int(join_type) + 1
    res_str = str(number_type)
    result_list = [int(x) for x in res_str]
    return result_list


r = add_one([9, 9, 9])
print(r)
