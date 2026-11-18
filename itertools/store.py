from itertools import *

sizes = ["S","M","L"]
colors = ["Red","Blue","Black"]

newlist = list(product(sizes,colors))

for i,j in newlist:
    print(f"{i}-{j}")
