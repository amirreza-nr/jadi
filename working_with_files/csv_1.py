"""takes a csv file and prints the rows as strings without the commas"""

import csv

with open("sample.csv", "r", newline="") as f:
    data = csv.reader(f, quotechar="|", delimiter=",")
    for line in data:
        print(" ".join(line))
