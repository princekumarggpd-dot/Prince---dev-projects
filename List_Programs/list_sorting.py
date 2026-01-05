#Sorting of List
lw = [2,3,7,8,7,9]
for i in range(len(lw)):
    for j in range(1,len(lw)):
        if lw[i] < lw[j]:
            lw[i] = i            
print(lw)
#2nd method
print(sorted(lw))

         