import random
number_elements = random.randint(3, 10)

first_list = []

while len(first_list) < number_elements:
    first_list.append(random.randint(1, 1000))
print("Перший список:", first_list)

second_list = []

if len(first_list) >= 3:
    second_list.append(first_list[0])
    second_list.append(first_list[2])
    second_list.append(first_list[-2])

print("Другий список:", second_list)
