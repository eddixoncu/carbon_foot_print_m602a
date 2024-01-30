msg = "Roll the dice"
print(msg)
m = 10 * 5
print("result is", m)
m = 6 - 3
print("result is", m)
m = 68.75 * 0
print("result is", m)
m = 100 / 17
print("result is", m)
m = 100 % 17
print("result is", m)

zero = 0.0
try:
    m = 100 / zero
    print("result is", m)
except Exception as e:
    print('Something wrong happened', e)

m = 2 ** 3
print("result is", m)

x = 5
y = 3
print("result is", x * y)

x = 10
y = 15
print("Comparing == result is ", x == y)
print("Comparing != result is ", x != y)
print("Comparing <= result is ", x <= y)
print("Comparing >= result is ", x >= y)

x = 1.1 + 2.2
print("x is ", x)
print("x is ", x == 3.3)