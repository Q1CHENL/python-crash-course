# Focus first on writing code that you understand clearly,
# which does what you want it to do. Then look for more
# efficient approaches as you review your code.

# 4-1
pizzas = ['salami pizza', 'bacon streak pizza', 'pizza with bbq sauce']
for pizza in pizzas:
    print(f'I like {pizza.title()}')
print('I love pizza!')

# 4-2
big_cats = ['lion', 'tiger', 'leopard']
for cat in big_cats:
    print(f'{cat.title()} is fierce and cute in the same time')
print('They are all cats, big ones tho.')

# 4-3
for i in range(1, 21):
    print(i)

# 4-4
million = list(range(1, 1000001))
# for i in million:
#     print(i)

# 4-5
minimum = min(million)
maximum = max(million)
summation = sum(million)
print(f'max: {maximum}, min: {minimum}, sum: {summation}')

# 4-6
odd_under_20 = list(range(1, 20, 2))
for i in odd_under_20:
    print(i)

# 4-7
threes = list(range(3, 31, 3))
for i in threes:
    print(i)

# 4-8
cubes = ['1', '8', '27', '64', '125', '216', '343', '512', '729', '1000']
for i in cubes:
    print(i)

# 4-9
cubes_10 = list(i**3 for i in range(1, 11))
for i in cubes_10:
    print(i)

# 4-10
print('The first three items in the cubes are: ')
for i in cubes[0:4]:
    print(i)
print('Three items from the middle of the list cubes are: ')
for cube in cubes[3:7]:
    print(cube)
print('The last three items in the cubes are: ')
for cube in cubes[-3:]:
    print(cube)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(food)
