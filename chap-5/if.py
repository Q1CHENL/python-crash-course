# 5-1
passed = True
print('Did I passed? I think so.')
print(passed == True)

cat = 'leopard'
print('Is that a leopard 2? I predict yes')
print(cat == 'leopard 2')

#5-2
myname = 'Qichen Liu'
name_matched = myname.lower() == 'qichen liu'
print(f'Name matched: {name_matched}')

apple_devices = ['iPad', 'iPhone', 'MacBook']
print(f"Do I own an Apple Watch: {'Apple Watch' in apple_devices}")
if 'Mac Pro' not in apple_devices:
    print("I don't have a Mac Pro as well")

# 5-3
alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points.')
if alien_color == 'red':
    print()

# 5-4
alien_color_1 = 'green'
if alien_color_1 == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')

alien_color_2 = 'yellow'
if alien_color_2 == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')

# 5-5
alien_color_3 = 'red'
if alien_color_3 == 'green':
    print('You just earned 5 points!')
elif alien_color_3 == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

alien_color_4 = 'green'
if alien_color_4 == 'green':
    print('You just earned 5 points!')
elif alien_color_4 == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

alien_color_5 = 'yellow'
if alien_color_5 == 'green':
    print('You just earned 5 points!')
elif alien_color_5 == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')

# 5-6
age = 23
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'
print(f'The person is a(n) {stage}')

fruits = ['orange', 'apple', 'watermelon']
if 'banana' in fruits:
    print('I really like banana')
if 'orange' in fruits:
    print('I really like orange')
if 'apple' in fruits:
    print('I really like apple')
if 'strawberry' in fruits:
    print('I really like strawberry')
if 'peach' in fruits:
    print('I really like peach')

    
