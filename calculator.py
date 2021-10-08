def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operator, a,b):
    res = 0
    if operator == "multiply":
        res = multiply(a, b)
    elif operator == "divide":
        res = divide(a, b)
    elif operator == "add":
        res = add(a, b)
    elif operator == "subtract":
        res = subtract(a, b)

    return res
operator = input()
a = int(input())
b = int(input())
result = calculate(operator, a, b)
print(result)
