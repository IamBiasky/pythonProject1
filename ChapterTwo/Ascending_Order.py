number1 = float(input("Enter First Value: "))
number2 = float(input("Enter Second Value: "))
number3 = float(input("Enter Third Value: "))

minimum = number1
maximum = number1

print(number1)

if number2 < minimum:
    minimum = number2
    print(minimum)

if number2 > maximum:
    maximum = number2
    print(maximum)

if number3 > maximum:
    maximum = number3
    print(maximum)

if number3 < minimum:
    minimum = number3
    print(minimum)
