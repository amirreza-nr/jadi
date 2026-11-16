"""takes to nums and prints the result of their devision
    handles the error and doesn't crash."""


def divide(a, b):
    result = a / b
    return result


while True:
    try:
        num1 = int(input("Enter fisrt number: "))
        num2 = int(input("Enter second number "))

        if num2 == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("the second number cant be zero!")
    except ValueError:
        print("the inputs must be integer")

    else:
        print("Result:", divide(num1, num2))
        print("the code was compiled successfuly.")
        break
