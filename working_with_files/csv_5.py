import csv

with open("sample_3.csv",newline='') as file:
    data = csv.reader(file,skipinitialspace=False)
    for d in data:
        print(d)
