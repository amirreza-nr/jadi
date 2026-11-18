import itertools

kids = ["amir", "zahra", "hassan"]
ages = [5, 8]

for kid,age in itertools.zip_longest(kids,ages,fillvalue= "unknown"):
    print(kid,age)

