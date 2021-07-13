def check_vowels():
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    user_str = input("Please Enter a string value: ")

    if any(char in vowels for char in user_str):
        print("String contains a vowel")

    else:
        print("String does not contain a vowel")


def check_odd_or_even():
    user_int = int(input('Enter Your Number Here: '))

    if user_int % 2 == 0:
        print("Number is Even")

    elif user_int % 2 == 1:
        print("Number is Odd")


def number_sorting():
    values = [3, 2, 18, 0, 7, 6]
    values.sort()
    odd_number = []
    even_number = []

    for i in range(len(values)):
        if values[i] % 2 == 0:
            even_number.append(values[i])
        if values[i] % 2 == 1:
            odd_number.append(values[i])

    for i in odd_number:
        even_number.append(i)
    print(even_number)


check_vowels()
print()
check_odd_or_even()
print()
number_sorting()
