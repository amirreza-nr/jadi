capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}

try:
    country = input('enter the country you want to know the capital (case sensitive): ')
    print(f"the capital is {capitals[country]}")

except KeyError :
    print("the country is not in dict")

else:
    print("thanks for not causing any error, I also know the finally syntax,will show it to you in the next project")
