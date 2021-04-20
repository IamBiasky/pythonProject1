def user_phonebook(user_name=None, user_age=None, user_no=None):

    for counter in range(3):
        user_name = input(str("Please enter your Name: "))
        user_age = int(input("Please enter your Age: "))
        user_no = int(input("Please enter your Phone Number: "))
        contact = {"Name": user_name, "Age": user_age, "Phone Number": user_no}

        counter += 1

        return contact
