st = input()
'''lv1,uv1,d,lc1,uc1,s = 0,0,0,0,0,0
lv = ['a','e','i','o','u']
uv = ['A','E','I','O','U']
digits = ['1','2','3','4','5','6','7','8','9','0']
for i in range(len(st)):
    if st[i] in lv:
        lv1 = lv1+1
    elif st[i] in uv:
        uv1 = uv1+1
    elif (st[i] not in lv) and (st[i]>='a' and st[i]<='z'):
        lc1=lc1+1
    elif (st[i] not in uv) and (st[i]>='A' and st[i]<='Z'):
        uc1=uc1+1
    elif st[i] in digits:
        d=d+1
    else:
        s=s+1
print('lv',"-",lv1)
print('uv',"-",uv1)
print('lc',"-",lc1)
print('uc',"-",uc1)
print('d',"-",d)
print('s',"-",s)'''


#Using inbuilt functions
lv,lc,uv,uc,d,s = 0,0,0,0,0,0
for i in st:
    if i.isupper():
        if i in 'AEIOU':
            uv=uv+1
        else:
            uc=uc+1
    elif i.islower():
        if i in 'aeiou':
            lv=lv+1
        else:
            lc=lc+1
    elif i.isdigit():
        d=d+1
    elif(not i.isalnum()):
        s=s+1
print('lv',"-",lv)
print('uv',"-",uv)
print('lc',"-",lc)
print('uc',"-",uc)
print('d',"-",d)
print('s',"-",s)