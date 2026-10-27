while True:
    number = (input("enter the number: "))

    if number == 'q':
        break

    number = int(number)

    if (number % 3 == 0 and number % 5 == 0):
        print("Lengendary!")
    elif(number % 3 == 0):
        print("Majical!")
    elif(number % 5 == 0):
        print("Cursed!")
    else:
        print("Normal.")


#Too easy to undrestand,Too sleepy to explain
