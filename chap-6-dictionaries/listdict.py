# 6-8
pet_1 = {
    'kind': 'cat',
    'owner': 'kathy'
}
pet_2 = {
    'kind': 'dog',
    'owner': 'z'
}
pets = [pet_1, pet_2]
for pet in pets:
    print(f"{pet['owner']} owns a(n) {pet['kind']}")

# 6-9
fav_places = {
    'chen': ['germany', 'czech', 'france'],
    'zheng': ['xinjiang', 'new zealand', 'aus'],
    'kai':['frankfurt', 'austria', 'prag']
}

for name, places in fav_places.items():
    print(f"\n{name}'s fav places are:")
    for place in places:
        print(place)
        
# 6-11, 6-12
xian = {
    'country': 'china',
    'population': '8 millions',
    'fact': 'was capital of 13 dynasties'
}

munich = {
    'country': 'germany',
    'population' : '1.5 millions',
    'fact': 'I currently study and live here in munich'
}

yunan = {
    'country': 'china',
    'population': 'I do not know',
    'fact': 'I always wanna have a visit there'
}

nice = {
    'country': 'France',
    'population': '0.5 million I guess',
    'fact': 'Another place I wanna visit'
}

cities = {
    'xian': xian,
    'munich': munich,
    'yunnan': yunan,
    'nice': nice
}

for city, info in cities.items():
    print(f"{city.title()} is a city in {info['country']} with {info['population']} population. \nOne fun fact about it is " + 
          f"{info['fact']}\n")

