def skyline(*args):
    max = args[0]

    for n in args:
        if n > max:
            max = n

    return max

hights = []

while True:
    x = input("enter the hight of the building, N to end asking: ")
    if x == "N" or x == "n":
        break

    hights.append(int(x))

print(skyline(*hights))
