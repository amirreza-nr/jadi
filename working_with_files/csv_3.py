"""import csv

with open("sample_1.csv", 'r') as f:
    data = list(csv.reader(f))

print(data)
"""

import csv
with open('sample_1.csv', newline='') as f:
   reader = csv.reader(f)
   data_list = list(reader)

for data in data_list:
    print(data)
