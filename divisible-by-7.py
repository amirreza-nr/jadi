def cal(n,m):
    numbers = []
    for i in range(n,m+1):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)

    return numbers

def main():
    n = int(input("enter the lower number: "))
    m = int(input("enter the higer number: "))

    print("this programm will print out the numbers that are divisible by 7 but not 5 between the numbers you have entered.")
    print(cal(n,m))

main()
