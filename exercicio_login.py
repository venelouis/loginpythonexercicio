# Define a user and a password, and after verify if they are valid.

USER = 'venelouis'
PASSWORD = '123'

while True:
    username = input('Enter your username: ')
    password = input('Enter you password: ')

    if username == USER and password == PASSWORD:
            print('You are in!')
            break
    else:
          print('invalid username or password')