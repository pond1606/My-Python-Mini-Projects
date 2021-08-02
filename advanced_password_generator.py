"""Advanced Password Generator by Phan Huynh Thien Phuc
This program generates passwords that YOU CAN USE. Most of the password-generating
programs just create passwords with random characters and numbers. You won't want
a password like that, right? This program will ask you some easy questions and
use them to create a password for you. This way you can remember it more easily. Pretty cool, right?"""

import random

while True:
    elements_list = []  # We'll pick some elements in here to create the password.
    input("""Answer the following questions. Some of them will be used to generate your password.
If you don't know the answer, just press Enter to skip it.
Press Enter to start generating your password...""")

    lover = input("What's your lover's name? ").replace(" ", "")  # Strip all spaces
    if lover != '':
        elements_list.append(lover)
    number = input("What's your favorite single-digit number? ").replace(" ", "")
    if number != '':
        elements_list.append(number)
    pet = input("What's your pet's name? ").replace(" ", "")
    if pet != '':
        elements_list.append(pet)
    birthday = input("When is your birthday? (if it's June 16th type 1606) ")
    if birthday != '':
        elements_list.append(birthday)
    acc_type = input("What type of account is this? (e.g. Facebook, Google, Github,...) ").replace(" ", "")
    if acc_type != '':
        elements_list.append(acc_type)

    if len(elements_list) < 3:  # The list is too short, restart the process.
        input("""You didn't provide enough information to generate a password!
Press Enter to restart this process (and remember to tell more about yourself)...""")
        continue

    random.shuffle(elements_list)  # Shuffle the list to make it more randomized.
    password = elements_list[0] + elements_list[1] + elements_list[2]  # Take the first 3 elements.
    print(f"Here's your password: {password}")
    generate_again = input("Do you want to generate another password? (yes/no) ")
    if generate_again.lower().startswith('n'):
        print("Don't forget that password!")
        break
