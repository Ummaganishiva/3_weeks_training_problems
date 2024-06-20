
#Job sequence algorithm
nums = [(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
profit = [5,6,5,4,11,2] #ans : 17
n = len(nums)
'''
for i in range(len(profit)-1):
    for j in range(len(profit)-i):
        if profit[i] < profit[j]:
            profit[i],profit[j] = profit[j],profit[i]
            nums[i],nums[j] = nums[j],nums[i]
ma = 0
for i in range(n):
    p = profit[i]
    k = i
    for j in range(i+1,n):
        if nums[j][1] <= nums[k][0]:
            p = p+profit[j]
            k = j 
    if p > ma:
        ma = p
print(ma)
'''

#Another logic
n = len(nums)
l = profit.copy()
for i in range(1,n):
    for j in range(i):
        if nums[j][1] <= nums[i][0]:
            if l[j] + profit[i] >= l[i]:
                l[i] = l[j] + profit[i]
                #print(l)
print(max(l))


