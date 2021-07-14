# Given two integer numbers, return their product.
# If the product is greater than 1000, then return their sum.

num1_int = int(input("Please enter first integer: "))
num2_int = int(input("Please enter second integer: "))

product_int = num1_int * num2_int
sum_int = num1_int + num2_int

if product_int > 1000:
    print(sum_int)
