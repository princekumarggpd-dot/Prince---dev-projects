# Program to count no of ocurrance of char
def freq(s):
    if type(s) == str:
        w = input("Enter the character")
        if w in s:
            return s.count(w), ":", w
        else:
            print("Not found")

    else:
        print("Invalid Input")


print(freq("Hello"))


# Program to Count no of vowels & consonants
def vowel(ol):
    if type(ol) == str:
        for i in ol.lower():
            if i in "aeiou":
                print(f"Vowels are {i}")

    else:
        return "Invalid Input"


vowel("Prince")
e = "Hello"
print(e)
# Program to remove duplicate char


def rem(sr):
    emo = ""
    for i in sr:
        if sr.count(i) > 1:
            pass
        else:
            emo += i
    return emo


print(rem("Ransomware"))

# Program to convert uppercase of an dict key
# if condition satisfied
d = {"name": {"prince":9000,"prashant":6000,"ritika":7000}}
r ={}
for i,j in d.items():
    for k,o in j.items():
        if isinstance(o,int) and o>5000:
            r.setdefault(k.upper(),o)
print(r)
        
        

