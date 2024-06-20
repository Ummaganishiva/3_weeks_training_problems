
'''l = [4,3,4,5,6,1,0,6,7]
first = 0
last = 1
l1 = []
count = 0
while last<len(l):
    if l[first] < l[last]:
        if len(l1) > 0:
            small = min(l[first],l[last])
            for i in l1:
                count = count+(small-i)
        first = last
        last = last + 1
        l1 = []
    else:
            l1.append(l[last])
            last = last+1
if small < len(l):
    last = last-1
    
    if len(l1) > 0:
        small = min(l[first],l[last])
        for i in l1:
            count = count+(small-i)
print(count)

#some correction needed for above code
'''
#Rain water storing between buildings problem
l =[4,3,4,5,6,1,0,6,7]
c = 0
left = []
left = l.copy()
right = []
right = l.copy()
for i in range(1,len(l)):
    if left[i] < left[i-1]:
        left[i] = left[i-1]
for i in range(len(l)-2,0,-1):
    if right[i] < right[i+1]:
        right[i] = right[i+1]
for i in range(len(l)):
    m = min(left[i],right[i])
    c = c+(m-l[i])
print(c)