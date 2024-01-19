
kids_meal=float(input('What is the price of a child meal? $'))
adult_meal=float(input('What is the price of an adult meal? $'))
number_kids=int(input('How many children are there? '))
number_adults=int(input('How many adults are there? '))
sales_tax=float(input('What is the sales tax rate? '))

meal_subtotal= number_kids*kids_meal+number_adults*adult_meal
print(f'Subtotal: ${meal_subtotal: .2f}' )

tax=meal_subtotal*sales_tax/100
print(f'Sales Tax: ${tax: .2f}')

tip=input('Would you like to leave a tip? (Answer Yes or No) ')

if tip.lower() == 'yes':
    tip_amount=float(input('How much would you like to tip? $'))
    print('Thank you!')
else: 
    tip_amount= 0
    print('Okay cheapo >:(')

meal_total=meal_subtotal + tax + tip_amount

print(f'Total: ${meal_total: .2f}')
payment=float(input('What is the payment amount? $'))


change=payment-meal_total
print(f'Change: ${change: .2f}' )
