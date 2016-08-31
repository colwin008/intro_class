def add(num1, num2):
    return num1 + num2
def subtract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def divide (num1, num2):
    return num1 / num2
def modulo (num1, num2):
    return num1 % num2
def power (num1, num2):
    return num1 ** num2
def square (num1):
    return num1 ** 2

# print add (4,5)
# print subtract (4,5)
# print multiply (4,5)
# print divide (4,5)
# print modulo (4,5)
# print power (4,5)
# print square(4)

print add(add(4,5), subtract(9,6))
print subtract(divide (12, 2), 60)
print add(add(1,2), 3)
print square(add(1,2))
print multiply(divide(modulo(3,4),9),9)
print multiply(7, add(3,8))
print subtract(add(1,2),multiply(3, add(4,5)))
print power(3,add(2,3))
