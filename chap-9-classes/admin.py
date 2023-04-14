import user

class Previliges:
    def __init__(self):
        self.previliges = ['can add post', 'can delete post']
    
    def show_previliges(self):
        for p in self.previliges:
            print(p)

class Admin(user.User):
    def __init__(self, first_name, last_name, location, age):
        super().__init__(first_name, last_name, location, age)
        #self.previliges = ['can add post', 'can delete post']
        self.previliges = Previliges()
        
    def show_previliges(self):
        for p in self.previliges.previliges:
            print(p)
            
admin_1 = Admin('AD', 'MIN', 'NET', '9999')
admin_1.previliges.show_previliges()
            
