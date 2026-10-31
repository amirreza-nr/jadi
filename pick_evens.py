def pick_evens(*nums):
    evens = []

    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    return evens


n = int(input("how many nums: "))

nums = []

for _ in range(n):
    nums.append(int(input("enter: ")))

print(pick_evens(*nums))
