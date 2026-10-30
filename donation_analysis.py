donations = {"jadi":5555, "sara":1250, "far":12, "hasan":9 }

def donate_a(donate):
    sum = 0
    max = -1
    person = ''

    for name,amount in donate.items():
        sum += amount
        if amount > max:
            max = amount
            person = name

    return sum,(sum/len(donate)),person

total,average,name = donate_a(donations)

print(f"total amount is: {total}")
print(f"statisticly each person donated: {average}")
print(f"the person who donated the most was dear {name}")
