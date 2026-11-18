from itertools import *

female_guests = ["sara","maryam","nazanin"]
male_guests = ["ali", "reza"]

for num,guest in enumerate(chain(male_guests,female_guests),1):
    print(f"guest {num} :",guest)
