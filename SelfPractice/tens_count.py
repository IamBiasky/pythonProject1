tens_count = 0
counter = 0

first_int = int(input("Please enter first integer: "))
second_int = int(input("Please enter second integer: "))

while first_int > 10 and second_int < 20:
    if first_int == 10 or second_int == 10:
        tens_count += 1
    first_int -= 5
    second_int += 5
    counter += 1

print(tens_count)
print(counter)
print(first_int)
print(second_int)