s = input()
length = len(s)
n = int(input())
l = []
st = ""
query_list = []
for i in range(n):
    l.append(list(map(str,input().split())))
for i in l:
    k = int(i[1])%length
    if i[0] == 'L':
        st=st+s[k]
    else:
        st=st+s[length-k]
#print(st)
new = []
for i in range(length-n+1):
    #print(s[i:i+n])
    new.append(s[i:i+n])
for i in new:
    if sorted(i) == sorted(st):
        print("Yes")
        break
else:
    print("No")
    