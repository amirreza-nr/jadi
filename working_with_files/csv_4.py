import csv

data = csv.DictReader(open("sample_1.csv"))

for row in data:
    print(row)

"""reads a csvfile as a dictionary"""
