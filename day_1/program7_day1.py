'''num1=int(input())
num2=int(input())
print(abs(int((300/7)-(400/7))))
start = num1%7
for i in range(num1+7-start,num2,7):
    print(i,end=" ")'''
'''
n = int(input())
def prime(n):
    if n==1:
        return False
    c=0
    for i in range(2,(n//2)+1):
        if n%i == 0:
            c=c+1
    if c==0:
        return True
    else:
        return False
if prime(n):
    print(n)
else:
    while 1:
        n = n+1
        if prime(n):
            break
    print(n)
    '''
n = int(input())
def prime(n):
    f=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            f=1
            break
    if f!=1:
        print(n)
    else:
        n=n+1
        prime(n)
prime(n)