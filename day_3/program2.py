n = int(input())
mat = [input() for i in range(n)]
st = input()
i=0
j=0
if len(st)%n !=0:
    print("no")
else:
    flag = 0
    while j<n:
        i = j 
        while i < len(st):
            if st[i] in mat[j]:
                i = i+n
            else:
                flag = 1 
                break
        if flag == 1:
            break 
        j = j+1 
    if flag == 1:
        print("No")
    else:
        print("Yes")
            
        

n = int(input())
mat = [list(input()) for i in range(n)]
st = input()
flag = 0
for i in range(len(st)):
    if st[i] not in mat[i%n]:
        flag =1 
        print("No")
        break
    else:
        mat[i].remove(st[i])
if flag == 0:
    print("Yes")
