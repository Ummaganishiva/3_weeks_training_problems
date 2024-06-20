def isprime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True

l = list(map(int,input().split()))
sum = 0
for i in range(len(l)-1):
    index1 = l[i] 
    index2 = l[i+1]
    for j in range(index2,index1,-1):
        if isprime(j):
            #print(j)
            sum = sum+j
            break
print(sum)