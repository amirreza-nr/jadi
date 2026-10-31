def sum(*args):
    sum = 0
    for number in args:
        sum += number

    return sum

print(sum(1,2,3))
