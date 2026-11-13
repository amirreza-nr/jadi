items = ["apple","orange","bannana","grape"]

try:
    index = int(input("starts from 0: "))
    print(f"item {index} is : {items[index]}")
except ValueError:
    print("enter a valid integar number.")
except IndexError:
    print(f"the maximum index is {len(items)}")
