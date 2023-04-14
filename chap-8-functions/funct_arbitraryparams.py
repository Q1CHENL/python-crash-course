# 8-12
def sandwich_items(*items):
    print(f"The sandwich is made with: ")
    for item in items:
        print(item)
sandwich_items('mashroom', 'chichken', 'ham')

# 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
    user_profile = build_profile('albert', 'einstein',
    location='princeton',
    field='physics')
    print(user_profile)
    
my_info = build_profile('Qichen', 'Liu', location = 'Munich', Uni = 'TUM', major = 'informatics')
print(my_info)

# 8-14
def make_car(manufacturer, model, **car_dict):
    # car_dict = {'manufacturer': manufacturer, 'model':model} would not work
    car_dict['manufacturer'] = manufacturer
    car_dict['model'] = model
    return car_dict
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)