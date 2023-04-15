# 11-3
import unittest
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        self.annual_salary += amount

    # setUp() runs before each test method
    def setUp(self):
        self.employee = Employee('No', 'Body', 100000000)
          
    def test_given_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 100005000)
        
    def test_given_custom_raise(self):
        self.employee.give_raise(1)
        self.assertEqual(self.employee.annual_salary, 100000001)

class EmployeeTest(unittest.TestCase):
if __name__ == '__main__':
    unittest.main()

        