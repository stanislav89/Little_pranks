from city_functions import city_country, math_func
import unittest

'''
unittest for city_country in city_functions.py
'''
class TestCityCountry(unittest.TestCase):
	def test_city_country(self):
		format_city_country = city_country('Kyiv', 'Ukraine')
		self.assertEqual(format_city_country, 'Kyiv, Ukraine')

'''
unittest for math_func in city_functions.py
'''
class TestMathFucn(unittest.TestCase):
	def test_math_func(self):
		format_math_func = math_func(5, 10, "+")
		self.assertEqual(format_math_func, 15)

if __name__ == '__main__':
	unittest.main()
