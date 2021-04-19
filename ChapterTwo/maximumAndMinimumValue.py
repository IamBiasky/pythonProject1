number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

minimum = number1
maximum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3

print("The minimum value is", minimum)
print("The maximum value is", maximum)


