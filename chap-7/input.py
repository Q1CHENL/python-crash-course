# 7-1
car = input('What kind of car do you want to rent? ')
print(f'Let me see if I can find you a {car}.')

# 7-2
people_count = int(input('How many people are in dinner group? '))
if people_count > 8:
    print('You have to wait.')
else:
    print('Table is ready!')

# 7-3
number = int(input('Number: '))
if number % 10 == 0:
    print(f'{number} is a multiple of 10')
else:
    print(f'{number} is not a multiple of 10')

# 7-4 7-6
active = True
while active:
    topping = input('Pizza topping: ')
    if topping == 'quit':
        active = False
    else: 
        print('I ill add the toping')
        
msg = ''
while msg != 'quit':
    msg = input('Pizza topping: ')     
    print(f'I ill add the toping {topping}') 


while True:
    topping = input('Pizza topping: ')
    if topping == 'quit':
        break
    else: 
        print('I ill add the toping')
        
# 7-5
while True:
    age = int(input('Age: '))
    if age < 3:
        print('Free!')
    elif age <12:
        print('10$.')
    else:
        print('15$.')

# 7-7
while True:
    print('looping!')
        