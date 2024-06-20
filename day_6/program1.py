'''
l = list(map(int,input().split()))
s = set(l)
ma = 0
for i in s:
    c = l.count(i)
    if c > ma:
        ma = c 
        ele = i
print(ele)'''
'''
from collections import defaultdict
l = list(map(int,input().split()))
di = defaultdict(int)
print(di)
n = len(l)
for i in l:
    di[i]+=1
    if di[i]>n//2:
        print(i)
        break
        '''
'''
l = list(map(int,input().split()))
c = 1
w = l[0]
for i in range(len(l)-1):
    if l[i+1]!=w:
        c = c-1
        if c == 0:
            w = l[i+1]
            c = 1
    else:
        c = c+1
print(w)
'''

n = int(input())
l = list(map(int,input().split()))
s = (n*(n+1))//2
l_sum = sum(l)
print(s-l_sum)
        