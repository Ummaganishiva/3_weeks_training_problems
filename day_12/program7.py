s1 = "tu5g2k1h8"
s2 = "g5g8gd6h3"
num = ""
for i in s1:
    if i.isdigit():
        num = num+i 
for i in s2:
    if i.isdigit():
        num = num+i 
new = list(set(num))
for i in range(len(new)):
    k = int(new[i])
    new[i] = k
new.sort(reverse=True)
if new[-1]%2 == 0:
    for i in new:
        print(i,end="")
else:
    for i in range(len(new)-1,-1,-1):
        if new[i]%2 == 0:
            new[i],new[len(new)-1] = new[len(new)-1],new[i]
            break
    for i in new:
        print(i,end="")