import random
number_elements = random.randint(3, 10)

original_list = []

while len(original_list) < number_elements:
    original_list.append(random.randint(1, 1000))
print("Перший список:", original_list)

new_list = []

if len(original_list) >= 3:
    new_list.append(original_list[0])
    new_list.append(original_list[2])
    new_list.append(original_list[-2])

print("Другий список:", new_list)
