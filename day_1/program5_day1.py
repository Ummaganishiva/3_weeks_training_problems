st = input()
s=""
for i in st:
    i=i.lower()
    if i in 'aeiou':
        s=s+(i.upper())
    else:
        s=s+i
print(s)