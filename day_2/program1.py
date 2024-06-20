'''def calculate_sum(num):
    sum = 0
    while num>0:
        x= num%10
        sum=sum+x
        num = num//10
    return sum
n = int(input())
while(1):
    s = calculate_sum(n)
    while s > 9:
        s = calculate_sum(s)
    if s in [2,3,5,7]:
        print(n)
        break
    else:
        n = n+1'''
        
def calculate(num):
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
        n = n+1
