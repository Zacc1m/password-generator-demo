import string
import random


pass_list = []

def password_generator():
    pass_list_input = input("what is password for? ")
    pass_list.append(pass_list_input)

    print()

    print("Password Bank: ")
    print(pass_list)
    print()
    length = input("How long do you want your password: ")
    return int(length)

user_input = ''
while user_input != "x":

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    password_length = password_generator()


    for x in range(password_length):
        password.append(random.choice(password_characters))

    print()

    final_password = ''.join(password)
    print("password one (" + str(len(final_password)) + "):\t\t" + final_password )
    print()
    
    pass_list.append(final_password)
    print("Password Bank: ")
    print(pass_list)

    print()

    save = input("Do you want to save this password? (yes or no) ")

    print()

    if save == "yes":
        print("To copy the password highlight it then right click using your mouse and press copy ")

        print()

        print("Copy Here ----> \t" + final_password )
        print()
        
    elif save == "no":
        exit()

    ask = input("Do you want to create another password? ('x' to exit) ")
    if ask == "x":
        exit()
    print()

print()

add_pass = password_generator()
pass_list.append(add_pass)
print(add_pass)