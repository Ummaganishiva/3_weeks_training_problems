l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
'''l1.extend(l2)
l1.sort()
print(l1)'''

l3 = []
length1 = len(l1)
length2 = len(l2)
i=0
j=0
while i<length1 and j<length2:
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i=i+1
    else:
        l3.append(l2[j])
        j=j+1
while i<length1:
    l3.append(l1[i])
    i=i+1
while j<length2: 
    l3.append(l2[j])
    j=j+1
print(l3)