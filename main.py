"""
def greeting(name):
    return 'Goodbye ' + name


def greeting(name):
    return 'HEllo ' + name


print(greeting('data'))
"""


def square(number):
    return number * number


squared = square(9)
print("Square is ", squared)


def max_num(number1, number2):
    if number1 >= number2:
        return number1
    else:
        return number2


maximum = max_num(50, 50)
print("Max is ", maximum)
maximum = max_num(51, 50)
print("Max is ", maximum)
maximum = max_num(50, 52)
print("Max is ", maximum)


def calculate_tax(salary):
    if salary <= 20000:
        return 0
    elif 20000 < salary <= 50000:
        return salary * 0.1
    elif 50000 < salary <= 100000:
        return salary * 0.2
    else:
        return salary * 0.3


calculated_tax = calculate_tax(20000)
print('Calculated tax is ', calculated_tax)

calculated_tax = calculate_tax(20001)
print('Calculated tax is ', calculated_tax)
calculated_tax = calculate_tax(67000)
print('Calculated tax is ', calculated_tax)

calculated_tax = calculate_tax(130000)
print('Calculated tax is ', calculated_tax)


def reverse_string(string: str):
    # a slice that steps backwards, -1.
    return string[::-1]


txt = "AnimaL"
print('Reversed is', reverse_string(txt))


def average(numbers):
    divisor = len(numbers)
    accumulated = 0
    for n in numbers:
        accumulated += n

    return accumulated / divisor


list_numbers = [5, 2, 6, 8, 7]
avg = average(list_numbers)
print("average is ", avg)

