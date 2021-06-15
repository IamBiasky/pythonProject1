opt_1 = str('yes')
opt_2 = str('no')

name_str = str(input("Welcome to PyMedic! \nPlease enter your Full Name:\n"))

print(f'Hi! {name_str}, thank you for reaching out to us!')
user_prob_str = input("Please, what is your problem?:\n")

user_response = str(input("Have you had" ' ' + user_prob_str + ' ' 'before? (Yes/No):\n'))

if user_response == opt_1.capitalize():
    print("Well, you have it again")

else:
    if user_response == opt_2.capitalize():
        print("Well, you have it now")
    #
    # else:
    #     print("Please enter a valid response")
