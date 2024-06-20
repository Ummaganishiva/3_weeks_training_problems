
# Shifting characters in the string
'''
s = input()
num = int(input())
num = num%26
st = ""
for i in range(len(s)):
    k=ord(s[i]) - num
    if k<97:
        k=k+26
    st=st+chr(k)
print(st)'''

'''
s = input()
ma = 0
i = 0
while i<len(s):
    j = i
    c = 1
    while j+1<len(s) and ord(s[j+1]) == ord(s[j])+1:
        c = c+1
        j = j+1
    if c > ma:
        ma = c 
    i = j+1
print(ma)'''

s = input()
ma = 0
i = 0
c = 1
while i<len(s)-1:
    if ord(s[i+1]) == ord(s[i])+1:
       c = c+1
    else:
        if c > ma:
            ma = c
        c = 1
    i = i+1
if c > ma:
    ma = c
print(ma)