# Random password generator
import random

letters = 'QWERTYUIOPASDFGHJKLZXCVBNM' + 'qwertyuiopasdfghjklzxcvbnm'
symbols = '/?!*&^%$#@_-'


def generator(password):
    # Define the length of the password
    passl = int(input("What will be the length of the password? The range should be 8-25! "))

    if (passl < 8 or passl > 25) or (passl is not int):  # check the condition of the password length
        while passl < 8 or passl > 25:
            passl = int(input("What will be the length of the password? The range should be 8-25! "))
    password += random.choice(symbols)   # to get at least one symbol in password

    for i in range(passl):  # generate the password
        password += random.choice(letters + symbols)

    passlist = list(password)  # converting a string to list to make a random sequence
    random.shuffle(passlist)
    password = ''.join(passlist)  # returning back to string

    return password


password = ''
print('Your generated password:', generator(password))
