username = input('Enter a username:')
password = input('Enter a password:')

user_length = len(username)
pass_length = len(password)

letter_isdigit = False
letter_isupper = False
letter_islower = False

for letter in password:
    if letter.islower() :
        letter_islower = True
    elif letter.isupper():
        letter_isupper = True
    elif letter.isdigit():
        letter_isdigit = True