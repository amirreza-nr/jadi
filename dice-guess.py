from random import randint

dice = randint(1,7)

while True:
    answer = int(input("guess: "))
    if answer == dice:
        print("That's right!")
        break

    print("again!")

#chooses a random number from one to six and asks you to guess until you get it!
