import csv

file = open("sample_2.csv")
data = csv.reader(file, quotechar="|", delimiter=" ")

for i in data:
    print(" ".join(i))
