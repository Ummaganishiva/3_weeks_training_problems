'''
s = input()
st = ""
ma = 0
for i in range(len(s)):
    st = st+s[i]
    for j in range(i+1,len(s)):
        if s[j] not in st:
            st = st+s[j]
        else:
            break 
    if len(st) > ma:
        ma = len(st)
    st = ""
print(ma)
'''
s = input()
di = {}
st = ""
i = 0
ma = 0 
while i < len(s):
    while i<len(s):
        if s[i] not in st:
            st = st+s[i]
            di[st[i]] = i 
        else:
            if len(st)>ma:
                ma = len(st)
            st = ""
            break
        i = i+1
    i = di[s[i]]+1
print(ma)