l = [4,9,8,2,14,3,5,6]
n = len(l)
l1 = []
for i in range(n-2):
    new = [l[i],l[i+1],l[i+2]]
    print(new)
    new.sort()
    l[i:i+3] = new[0:]
    #print(new)
    l1.append(new[0])
l1.append(l[n-2])
l1.append(l[n-1])
print(l1)
'''
l = [4,9,8,2,14,3,5,6]
n = len(l)
for i in range(n-2):
    if l[i] > l[i+1]:
        l[i],l[i+1] = l[i+1],l[i]
    if l[i+1] > l[i+2]:
        l[i+1],l[i+2] = l[i+2],l[i+1]
    if l[i] > l[i+1]:
        l[i],l[i+1] = l[i+1],l[i]
print(l)
'''