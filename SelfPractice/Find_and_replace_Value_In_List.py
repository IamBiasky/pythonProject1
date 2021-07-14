# Given a Python list, find the value 20 in the list,
#  and if it is present, replace it with 200. Only update
# the first occurrence of the value.

list_of_numbers = [1, 20, 30, 27, 45, 35, 15]

counter = 0

print(list_of_numbers)

for value in list_of_numbers:
    counter += 1
    if value == 20:
        list_of_numbers[counter - 1] = 200
        break
print(list_of_numbers)