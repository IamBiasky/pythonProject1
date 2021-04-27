number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

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

sum_int = minimum + maximum
product_int = minimum * maximum
average_int = (number1 + number2 + number3) / 3

print("The sum is: ", sum_int)
print("The product is: ", product_int)
print("The average is: ", average_int)
