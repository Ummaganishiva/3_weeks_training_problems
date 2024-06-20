'''def calculate(num):
    if num<=0:
        return 0
    return (num%10)+calculate(num//10)
n = int(input())
while(1):
    s = calculate(n)
    while s > 9:
        s = calculate(s)
    if s in [2,3,5,7]:
        print(n)
        break
    else:
        n = n+1'''
'''
def sum1(li,i):
    if i == len(li):
        return 0 
    return li[i]+sum1(li,i+1)
l = list(map(int,input().split()))
print(sum1(l,0))'''

'''
def sum1(l1,l2,i,even,odd):
    if i == len(l1):
        return [even,odd]
    if l1[i]%2 == 0:
        even = even+l1[i]
    if l2[i]%2 !=0:
        odd = odd+l2[i]
    return sum1(l1,l2,i+1,even,odd)
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(sum1(l1,l2,0,0,0))'''

def sum1(l1,l2,i,j,even,odd):
    if i == len(l1) and j == len(l2):
        return [even,odd]
    if i<len(l1) and l1[i]%2 == 0:
        even = even+l1[i]
    if j<len(l2) and l2[j]%2 !=0:
        odd = odd+l2[j]
    if i < len(l1) and j < len(l2):
        return sum1(l1,l2,i+1,j+1,even,odd)
    elif i == len(l1):
        return sum1(l1,l2,i,j+1,even,odd)
    if j == len(l2):
        return sum1(l1,l2,i+1,j,even,odd)
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(sum1(l1,l2,0,0,0,0))





