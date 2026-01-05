#remove duplicates in list
l = ["apple","banan",2,2]
dp =[]
for i in l:
    if i not in dp:
        dp.append(i)
print(f"The new list is {dp}")
#2nd Method
e = list(set(l))
print(e)
#3rd Method
for i in l:
    if l.count(i)>1:
        print(i)
l.pop(len(l)-1)       
print(l)


  

    