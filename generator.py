import random
import string

# TODO: add comments // try and see if i can create as functions

password_length = None
no_of_upper_letters = None
no_of_lower_letters = None
no_numbers = None


while password_length == None:
    try:
        password_length = int(input("length of your password: "))

        if password_length < 6:
            print("to short must be greater than 6.")
            password_length = None

    except ValueError:
        print("enter integer values only.")
        password_length = None

while no_of_upper_letters == None and no_of_lower_letters == None and no_numbers == None:
    try:
        no_of_upper_letters = int(input("number of upper letters: "))
        no_of_lower_letters = int(input("number of lower letters: "))
        no_numbers = int(input("how many numbers: "))

        if password_length < no_of_upper_letters + no_of_lower_letters + no_numbers + 1 > password_length:

            print(
                f"combination must sum up to password length {password_length}")
            no_of_upper_letters = None
            no_of_lower_letters = None
            no_numbers = None

    except ValueError:
        print("enter integer values only.")
        no_of_upper_letters = None
        no_of_lower_letters = None
        no_numbers = None


upper_letters = "".join(random.choice(string.ascii_uppercase)
                        for i in range(no_of_upper_letters))

lower_letters = "".join(random.choice(string.ascii_lowercase)
                        for i in range(no_of_lower_letters))

numbers = "".join(random.choice(string.digits) for i in range(no_numbers))

symbols = "".join(random.choice(string.punctuation))

mixed_ = [upper_letters, lower_letters, numbers, symbols]
random.shuffle(mixed_)
password = "".join(mixed_)
print(f"Your new password is: {password}")
