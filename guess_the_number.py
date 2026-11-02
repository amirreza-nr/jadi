from random import randint


win = False
num = randint(1,100)
counter = 0
record = 0

def announcer():
    print("there you go!")
    print(f"got it in {counter} times!")

def compare(user):
    global record

    if user == num:

        announcer()
        return True

    if user > num:
        print("it's smaller!")
    if user < num:  # saying the user wont insert a negative number.
        print("it's bigger")
    return False

def guess():
    while True:
        num = int(input("enter your number:"))
        if num <= 0 : # checks if the number is positive
            print ("not valid , try again: ")

            continue

        return num

def ask():
    ans = input("wanna try again? [Y/N]: ")
    global counter

    if ans.upper() == 'Y':
        counter = 0
        return False


    return True

def record_calculate(counter,record):

    if record == 0 or record > counter:
        print(f"new record! it's {counter}")
        record = counter
    return None



while not win:
    counter += 1

    user_guess = guess()

    win = compare(user_guess)

    if win == True:
        record_calculate(counter,record)
        win = ask()
