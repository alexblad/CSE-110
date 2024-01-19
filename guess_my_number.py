import random

magic_number=random.randint(1,100)
guess_number=-1

while guess_number != magic_number:
    guess_number=int(input('What is your guess?'))

    if guess_number> magic_number:
        print('Lower')
    elif guess_number< magic_number:
        print('Higher')
    else:
        print('Correct!')
 
