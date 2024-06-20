st = input()
u,l,d,s=0,0,0,0
for i in st:
    if i.isupper():
        u=1
    elif i.islower():
        l=1
    elif i.isdigit():
        d=1
    elif (not i.isalnum()):
        s=1
li = [u,l,d,s]
if len(st)>=8 and sum(li)==4:
    print('-1')
elif len(st)>=8:
    print(li.count(0))
else:
    print(max(li.count(0),8-len(st)))

'''
if u>=1 and l>=1 and d>=1 and s>=1 and len(st)>=8:
    print("It is valid password")
else:
    if len(st)<8:
        co=0
        for j in li:
            if j==0:
                co=co+1
        if co<(8-len(st)):
            print(8-len(st))
        else:
            print(co)
    else:
        co=0
        for j in li:
            if j == 0:
                co=co+1
        print(co)'''