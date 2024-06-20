'''
n = int(input())
k = 1
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1) or (j==0 or j==n-1):
            print("*",end="  ")
        else:
            print(k,end="  ")
            k=k+1 
    print()
'''
'''
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print("-",end="")
    k = 97
    for j in range(i+1):
        print(chr(k),end="")
        k = k+1
    k = k-1
    for j in range(i):
        print(chr(k-1),end="")
        k=k-1
    for j in range(n-i-1):
        print("-",end="")
    print()
'''
'''
n = int(input())
for i in range(1,2*n):
    if i>=5:
        i = 2*n-i
    for j in range(1,i):
        print(j,end=" ")
    for j in range(1,2*(n-i)+2):
        print(i,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
'''

n = int(input())
for i in range(1,2*n):
    for j in range(1,2*n):
        print(min(i,j,2*n-i,2*n-j),end=" ")
    print()
        
    









        