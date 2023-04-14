# 9-1, 9-2, 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaureant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restuarant(self):
        print(self.restaureant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print("The restaurant is open!")
    
    def increment_number_served(self, served):
        self.number_served += served
        
    
restaurant_0 = Restaurant('CuisineCenter', 'Noodle')
print(restaurant_0.restaureant_name)
print(restaurant_0.cuisine_type)
restaurant_0.describe_restuarant()
restaurant_0.open_restaurant()    

restaurant_1 = Restaurant('Seen', 'Pork')
restaurant_2 = Restaurant('MamaBao', 'Nudel')
restaurant_3 = Restaurant('Honghong', 'Rice')
restaurant_1.describe_restuarant()
restaurant_2.describe_restuarant()
restaurant_3.describe_restuarant()

restaurant = Restaurant('Yanyu', 'Beef')
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 1
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(100)
print(f"Number served: {restaurant.number_served}")

# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Coco', 'Strawberry', 'Original']
        
    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)
icecream_stand = IceCreamStand('IceCreamQueen', 'Icecream')
icecream_stand.print_flavors()

    
