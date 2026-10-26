file = open("dummy.txt","r")
print(type(file))
file.close()

new = open("new.txt","w")
new.write("i creatin this file after i just closed dummy.txt")
new.close()

print("there was no fileio exercise in jadi course so i just made one!")
