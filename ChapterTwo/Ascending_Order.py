number1 = float(input("Enter First Value: "))
number2 = float(input("Enter Second Value: "))
number3 = float(input("Enter Third Value: "))

num1 = min(number1, number2, number3)
num3 = max(number1, number2, number3)
num2 = (number1 + number2 + number3) - num3 - num1

print("Numbers in Ascending Order: ", num1, ",", num2, ",", num3)

# minimum = number1
# maximum = number1

# print(minimum)

# if minimum > number2:
#  minimum = number2
# print(minimum)


# if minimum > number3:
# minimum = number3
# print(minimum)

# if number2 < number3:
#  minimum = number2
# print(minimum)

# else:
#  if number2 > number3:
#     minimum = number3
#    print(minimum)

# if number3 > number2:
#   minimum = number2
#  print(maximum)
