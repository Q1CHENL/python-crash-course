# 6-1
me_dict = {
    'first_name': 'qichen',
    'last_name': 'liu',
    'age':  '22',
    'city': 'munich'
}
# 6-7
mom_dict = {
    'first_name': 'h',
    'last_name': 'z',
    'age': '51',
    'city': 'xian'
}

grandma_dict = {
    'first_name': 'x',
    'last_name': 't',
    'age': '75+',
    'city': 'changan'
}

people = {
    'chen': me_dict,
    'mom': mom_dict,
    'nanny': grandma_dict
}

for p, p_dict in people.items():
    print(f'Person: {p}')
    full_name = f"{p_dict['first_name']} {p_dict['last_name']}"
    age = f"{p_dict['age']}"
    location = f"{p_dict['city']}"
    print(f'{full_name}, {age}, lives in {location}')

print(me_dict['first_name'].title())
print(me_dict['last_name'].title())
print(me_dict['age'])
print(me_dict['city'])

# 6-2, 6-10
fav_nums = {
    'Ann': [1, 3],
    'Bob': [2, 42],
    'Cide': [3],
    'Dave': [4],
    'Edy': [5]
 }
# for p in fav_nums:
#     print(f'Fav num of {p} is {fav_nums[p]}')
for p, nums in fav_nums.items():
     print(f'\nFav num of {p} are:')
     for num in nums:
         print(num)

# 6-3, 6-4
programming_words = {
    'for': 'loop',
    'list': 'array',
    'dict': 'map',
    'print': 'output',
    'if': 'condition',
    'set': 'no duplicates',
    'while': 'another loop',
    'f': 'format',
    "\\n": 'newline',
    '{}': 'var'
}
for pw in programming_words:
    print(f'\n{pw}: {programming_words[pw]}')

# 6-5
rivers = {
    'nile': 'egypt',
    'huanghe': 'china',
    'missisippi': 'us'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')
for river in rivers:
    print(river)
for country in rivers.values():
    print(country)

# 6-6
should = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'chen': 'c++',
    'phil': 'python',
}

took = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in should:
    if name in took:
        print(f'Thank you {name.title()}')
    else:
        print(f'{name.title()}, take it boy!')


