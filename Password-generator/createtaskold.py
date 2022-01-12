import string
import random

letters = string.ascii_lowercase
letters2 = string.ascii_uppercase
digits = string.digits  
punctuation = string.punctuation

def get_password_length():
    length = input("How long do you want your password: ")
    return int(length)

def password_generator(length=8):
    ask_user1 = input("Do you want lowercase letters (yes or no) ")
    if ask_user1 == "yes":
        result1 = ''.join(letters)

    ask_user2 = input("Do you want upercase letters (yes or no) ")
    if ask_user2 == "yes":
        result2 = ''.join(letters2)

    ask_user3 = input("Do you want numbers (yes or no) ")
    if ask_user3 == "yes":
        result3 = ''.join(digits)

    ask_user4 = input("Do you want special characters (yes or no) ")
    if ask_user4 == "yes":
        result4 = ''.join(punctuation)
    
    result = (result1 + result2 + result3 + result4)


    result = list(result)
    
    random.shuffle(result)


    random_password = random.choices(result, k=length)
    random_password = ''.join(random_password)
    return random_password


password_length = get_password_length()
password_one = password_generator(password_length)

print("password one (" + str(len(password_one)) + "):\t\t" + password_one )
#print("password one (" + str(len(password_two)) + "):\t\t" + password_two )
