number = int(input("enter: "))

while number != 1:
    if number % 2 == 0:
        number = number / 2
    else:
        number = (number * 3) + 1

    print(int(number))

#a simple project to practice while structure, figure out what it does for yourself :|
