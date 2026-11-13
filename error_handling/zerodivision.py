def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Warning: Division by zero is not allowed.")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # None
