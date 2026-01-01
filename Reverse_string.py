# Program to reverse a String
s = input("Enter the string")
print(s[::-1])

# 2nd Method
t = " "
for i in range(len(s) - 1, -1, -1):
    t += s[i]
print("h", t)


# 3rd Method
def string(e):
    re = ""
    for n in e:
        re = n + re
    return re


print(string("Goat"))
