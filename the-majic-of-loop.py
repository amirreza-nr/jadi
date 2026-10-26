n = int(input("please enter the number of steps steps: "))
x = int(input("please enter the intial number: "))

for i in range(n):
    if x % 2 == 0:
        x = x/2
    else:
        x = (x*2) - 1

print(int(x))

"""takes two inputs one as the number and on as the number of steps
    if the number was even it divides it by 2 otherwise it muptiplies it by 2 then subtracts 1"""
