def prime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True
n = int(input())
start = 1
end = n-1
f = 0
while start<=end:
    if prime(start) and prime(end):
        print(start,end,"Yes they Form")
        f = 1
        break
    else:
        start = start+1
        end = end-1
if f == 0:
    print("No they can't form")
        