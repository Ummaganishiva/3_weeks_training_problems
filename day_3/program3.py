l = list(map(int,input().split()))
n = len(l)
ma = 0
'''
for i in range(n):
    for j in range(i+1,n):
        if l[j] - l[i] > ma:
            ma = l[j] - l[i]
print(ma)'''
i = 1
j = 0
while i<n:
    if l[i]-l[j]<0:
        j = i
    else:
        if l[i]-l[j]>ma:
            ma = l[i]-l[j]
    i=i+1
print(ma)
