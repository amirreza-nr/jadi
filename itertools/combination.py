import itertools

players = ["Messi","Ronaldo","Neymar","Mbappe"]
for team in itertools.combinations(players,2):
    print(team)

print("".center(50,'-'))

digits = [1,2,3]
for password in itertools.permutations(digits,3):
    print(password)
