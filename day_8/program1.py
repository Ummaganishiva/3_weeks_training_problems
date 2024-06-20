'''
nums = list(map(int,input().split()))
n = len(nums)
temp = []
l = []
c = 0
i = 0
while 1:
    #print(nums)
    for i in nums:
        if i not in temp:
            c = c+1
            temp.append(i)
        else:
            continue
    for i in temp:
        nums.remove(i)  
    #print(temp)
    l.append(temp)
    temp = []
    if c == n:
        break
print(l)
'''
from collections import defaultdict
l = list(map(int,input().split()))
di = defaultdict(int)
res = []
for i in l:
    di[i]+=1
while 1:
    temp = []
    for i in di:
        if di[i]>0:
            temp.append(i)
            di[i]-=1
    if len(temp)>0:
        res.append(temp)
    else:
        break
print(res)