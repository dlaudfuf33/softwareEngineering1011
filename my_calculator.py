# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y * 2  # 수정된 부분

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y
