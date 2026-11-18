import itertools

def generate_id(num):
    return itertools.count(num)


x = generate_id(1)

for i in range(5):
    print(next(x))
