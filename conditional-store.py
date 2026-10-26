amount = float(input("enter: "))

if amount > 50000:
    amount = amount - (amount* 1/5)
#if the price was more than 50k,give twenty percent discount

elif 50000 >= amount >= 20000:
    amount = amount - amount/10

#if the price was between 20k and 50k, give ten percent discout

print(amount)
