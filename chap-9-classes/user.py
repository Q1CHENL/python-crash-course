# 9-3, 9-5
class User:
    def __init__(self, first_name, last_name, location, age):
        self.fisrt_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"Full name: {self.fisrt_name} {self.last_name}")
        print(f"Address: {self.location}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        print(f"Hi, {self.fisrt_name} {self.last_name}!")
        
Qichen = User('Qichen', 'Liu', 'Munich', '22')
Kai = User('Zekai', 'Li', 'Munich', '22')
Qichen.greet_user()
Qichen.describe_user()
Kai.greet_user()
Kai.describe_user()

Qichen.increment_login_attempts()
print(f"Qichen's number of login attempts: {Qichen.login_attempts}")
Qichen.reset_login_attempts()
print(f"Qichen's number of login attempts: {Qichen.login_attempts}")

# 9-8
class Previliges:
    def __init__(self):
        self.previliges = ['can add post', 'can delete post']
    
    def show_previliges(self):
        for p in self.previliges:
            print(p)


# 9-7
class Admin(User):
    def __init__(self, first_name, last_name, location, age):
        super().__init__(first_name, last_name, location, age)
        #self.previliges = ['can add post', 'can delete post']
        self.previliges = Previliges()
        
    def show_previliges(self):
        for p in self.previliges.previliges:
            print(p)
admin = Admin('ad', 'min', 'net', '9999')
#admin.show_previliges()
    
admin_1 = Admin('AD', 'MIN', 'NET', '9999')
admin_1.previliges.show_previliges()


