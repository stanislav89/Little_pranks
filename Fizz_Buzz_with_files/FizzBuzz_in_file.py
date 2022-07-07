''' Написать fizzbuzz для 10 троек чисел, которые записаны в файл.
Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.
Результат должен записываться в другой файл '''

''' Write fizzbuzz for 10 triplets of numbers that are written to the file.
Read the first line from the file, take numbers from it, count fizzbuzz for them, and output.
The result should be written to another file '''

data = []
with open('FizzBuzz_numbers') as f:
    for line in f:
        data.append([int(x) for x in line.split()])

result_file = open('FizzBuzz_result', 'w')
for numbers in data:
    result_file.write('\n*** FizzBuzz for ' + str(numbers) + ' numbers: ')
    i = 1
    while i <= numbers[2]:
        if i % numbers[0] == 0 and i % numbers[1] == 0:
            result_file.write('FB ')
        elif i % numbers[0] == 0:
            result_file.write('F ')
        elif i % numbers[1] == 0:
            result_file.write('B ')
        else:
            result_file.write(str(i) + ' ')
        i += 1
