number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))
number4 = int(input("Enter fourth integer: "))

smallest_int = min(number1, number2, number3, number4)
largest_int = max(number1, number2, number3, number4)

sum_int = smallest_int + largest_int
product_int = smallest_int * largest_int
average_int = (number1 + number2 + number3 + number4) / 4

print("The sum is: ", sum_int)
print("The product is: ", product_int)
print("The average is: ", average_int)
