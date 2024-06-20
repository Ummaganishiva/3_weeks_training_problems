l1 = list(map(int,input().split()))
temp = []
for i in range(len(l1)):
    if l1[i] not in temp:
        temp.append(l1[i])
        print(l1[i],"-",l1.count(l1[i]))
    