#sunrise falling on buildings
l = [3,4,5,10,4,3]
n = len(l)
morning = []
morning.append(l[0])
const = l[0]
for i in range(1,len(l)):
    if l[i] > l[i-1] and l[i] > const:
        morning.append(l[i])
        const = l[i]
evening = []
evening.append(l[n-1])
const = l[n-1]
for i in range(len(l)-2,-1,-1):
    if l[i] > l[i+1] and l[i] > const:
        evening.append(l[i])
        const = l[i]
print(morning,evening)
