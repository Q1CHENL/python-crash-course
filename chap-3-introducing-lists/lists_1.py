# 3-1
friends = ['Li Zekai', 'Noah', 'Nick']
for i in range(len(friends)):
    print(friends[i])

# 3-2
for name in friends:
    print(f'What up, {name}?')

# 3-3
vehicles = ['fighter jet', 'bike', 'dream']
print(f'The best vehicle is your {vehicles[2]}')

# 3-4
invited = ['LBJ', 'The Weeknd', 'Mom']
print(
    f'Hi {invited[0]}, you are my fav athelet, I wanna invite you to dinner!')
print(
    f'Yo {invited[1]}, my fav singer, would you like to have dinner together?')
print(f'{invited[2]}, dinner is ready!')

# 3-5
print(f'Unfortunately {invited[0]} can not make it due to a NBA game tonight.')
invited[0] = 'Kai'
print(f'Hi {invited[0]}, Kai let us have dinner!')
print(
    f'Yo {invited[1]}, my fav singer, would you like to have dinner together?')
print(f'{invited[2]}, dinner is ready!')

print('Hallo Zusammen, ich habe ne groesseren Tisch gefunden! Wir koennen mehr Leuten haben!')
invited.insert(0, 'Dad')
invited.insert((int)(len(invited) / 2), 'Grandma')
invited.append('Grandpa')
for person in invited:
    print(f'Welcome, {person}!')

# 3-7
print('Ops I can only invite 2 people')
for i in range(len(invited) - 2):
    print(f'Sorry! Maybe next time! Bye, {invited.pop()}!')
num = len(invited)
for person in invited:
    print(f'{person}, you are still in!')

del invited[1]
del invited[0]

print('Remaining guests: ' + str(len(invited)))

# 3-8
locations = ['Xin Jiang', 'Yun Nan', 'Milan', 'Nice']
print(locations)
print(sorted(locations))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.reverse()
print(locations)

# 3-9
print(f'{num} persons are still coming')

# 3-10
programming_languages = ['javascript', 'dart', 'swift']
original = programming_languages.copy()
o_sorted = sorted(original)
programming_languages.sort()
reversed = programming_languages.reverse()
print(o_sorted)
print(programming_languages)

# 3-11
err_index = len(programming_languages)
print(programming_languages[err_index - 1])
