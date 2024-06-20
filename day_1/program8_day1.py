'''n = int(input())
c=0
def prime(n):
    if n == 1 or n == 0:
        return False
    co = 0
    for i in range(2,(n//2)+1):
        if n%i == 0:
            co=co+1
    if co == 0:
        return True
    else:
        return False
while n>0:
    x = n%10
    if prime(x):
        c=c+1
    n = n//10
print(c)'''
c=0
n = int(input())
while n>0:
    x = n%10
    if x in [2,3,5,7]:
        c=c+1
    n=n//10
print(c)