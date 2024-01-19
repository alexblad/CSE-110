print('Please enter the following information: ')
#This prints a blank line
print()

First_Name= input('First name: ')
Last_Name= input('Last name: ')
Email= input('Email address: ')
Phone= input('Phone number: ')
Job_title= input('Job title: ')
ID_number= input('ID Number: ')

#\n can also be used to make a blank line
print('\nThe ID Card is: ')
print('-------------------------------------------')
Line_1= f'{Last_Name.upper()}, {First_Name.capitalize()}'
print(Line_1)
Line_2=f'{Job_title.title()}'
print(Line_2)
Line_3=f'ID: {ID_number}'
print(Line_3 )
print()
Line_4=f'{Email.lower()}'
print(Line_4)
print(Phone)
print('-------------------------------------------')