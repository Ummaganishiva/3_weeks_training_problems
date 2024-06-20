#Given a list representing amount of gold in houses and a thief travels every house and steals gold. but should not go adjacent house, determine the max profits he can achieve
'''
l = list(map(int,input().split()))
n = len(l)
def fun(l,i,j,ma,n):
    c = 0
    if i == n-1:
        return ma 
    elif j == n or j>n:
        i = i+1
        j = i+2
    else:
        c =c+l[i]
        for k in range(j,n,2):
            c = c+l[k]
        if c > ma:
            ma = c
        j=j+1
    return fun(l,i,j,ma,n)
print(fun(l,0,2,0,n))
'''
#Another type of approach
def fun(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l)
    le = l[0] + fun(l[2:])
    re = l[1] + fun(l[3:])
    return max(le,re)
print(fun(list(map(int,input().split()))))