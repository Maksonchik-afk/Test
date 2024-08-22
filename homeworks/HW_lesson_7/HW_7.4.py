def common_elements():
		list_of_3 = {i for i in range(0, 101) if i % 3 == 0}
		list_of_5= {i for i in range(0, 101) if i % 5 == 0}
		return list_of_3.intersection(list_of_5)


print(common_elements())
