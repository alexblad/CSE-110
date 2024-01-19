
first_rider_age = int(input('What is the age of the first rider? '))
if first_rider_age >= 18:
    rider_one_age = True 
else: rider_one_age = False

first_rider_height = int(input('What is the height of the first rider? '))
if first_rider_height >= 62:
    rider_one_height = True
else: rider_one_height = False

second_rider = input('Is there a second rider? (yes/no)? ')
if second_rider.lower() == 'yes':
    second_rider = True
    second_rider_name = input('What is the second riders name? ')
else:
    second_rider = False


if second_rider:
    second_rider_age = int(input('what is the age of the second rider? '))
    second_rider_height = int(input('what is the height of the second rider? '))
    if (second_rider_age >=18 or rider_one_age) and (first_rider_height >= 36 and second_rider_height >= 36):
        print('welcome to the ride')
    else:
        print('nope, not today')       
else:
    if rider_one_age and rider_one_height:
        print('Welcome to the ride! be safe and have fun! ')
    else:
        print('sorry, you may not ride, loser.')