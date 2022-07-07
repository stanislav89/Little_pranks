''' У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz.
До третьего необходимо досчитать от единицы. Считая, надо выводить число.
Если число кратно fizz - надо выводить F вместо числа. Если число кратно buzz - надо выводить B вместо числа.
Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число '''

''' You have three numbers, they are entered from the console. The first number is called fizz, the second is called buzz.
To the third must be counted from one. Counting, you need to output a number.
If the number is a multiple of fizz, print F instead of the number. If the number is a multiple of buzz, you should output B instead of the number.
If the number is a multiple of both fizz and buzz, output FB. And so - until the third entered number is reached '''

fizz = int(input('Enter the first number: '))
buzz = int(input('Enter the second number: '))
third = int(input('Enter the third number: '))

i = 1
while i <= third:
    if i % fizz == 0 and i % buzz == 0:
        print('FB', end=' ')
    elif i % fizz == 0:
        print('F', end=' ')
    elif i % buzz == 0:
        print('B', end=' ')
    else:
        print(i, end=' ')
    i += 1
