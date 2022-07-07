def city_country(city=input("Enter the CITY name: "), country=input("Enter the COUNTRY name: ")):
	full_city_country = city + ', ' + country
	return full_city_country.title()

def math_func(a=int(input("Enter the FIRST number: ")), b=int(input("Enter the SECOND number: ")), operation="+"):
	operation = input("Enter the operation with A and B (+ - / *): ")
	if operation == "-":
		return a - b
	elif operation == "*":
		return a * b
	elif operation == "/":
		return a / b
	else:
		return a + b

if __name__ == '__main__':
	city_country()
	math_func()
