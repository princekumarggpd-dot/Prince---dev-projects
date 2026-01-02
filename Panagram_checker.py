# Program to check Panagram
sentence = "I live in San Fransico and want to live luxuiours life"
for t in sentence:
    if t.lower() not in "abcdefghijklmnopqrstuvwxyz":
        break
else:
    print("Its a panagram")


# method 2
def chekr(n):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in n:
        if i.upper() not in alp:
            break
    else:
        print("Panagram")


chekr("abcdefghijklmnopqrstuvwxyz")
