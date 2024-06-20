str1 = input()
'''i=0
k = str1[0]
j=0
while i<len(str1): 
    if str1[i]==k:
        j=j+1
    else:
        print(k,end="")
        print(j,end="")
        j=1
        k = str1[i]
    i=i+1
print(k,end="")
print(j,end="")'''

c=1
s = ""
for i in range(len(str1)-1):
    if str1[i] == str1[i+1]:
        c=c+1
    else:
        s=s+str1[i]+str(c)
        c=1
s=s+str1[i+1]+str(c)
print(s)
        
    