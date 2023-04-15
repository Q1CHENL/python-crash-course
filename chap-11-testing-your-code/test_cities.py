# 11-1, 11-2
import unittest
from city_functions import city_country

class CityTest(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country('munich', 'germany'), 'Munich, Germany')
    
    def test_city_country_population(self):
        self.assertEqual(city_country('xian', 'China', '9000000'), 'Xian, China - population 9000000')
if __name__ == '__main__':
    unittest.main()
        
