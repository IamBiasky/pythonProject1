def exponent(base, exp):
    exp_int = base ** exp
    return exp_int


base = int(input("Please enter a base integer: "))
exp = int(input("Please enter an exponent integer: "))

print(exponent(base, exp))
