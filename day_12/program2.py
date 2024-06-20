'''l = [3,4,7]
num = 10
mat = [[0]*(num+1) for i in range(len(l)+1)]
for i in range(len(l)+1):
    for j in range(num+1):
        if i == 0:
            mat[i][j] = j 
        elif l[i-1] > mat[0][j]:
            mat[i][j] = mat[i-1][j]
        else:
            mat[i][j] = mat[i][(mat[0][j] - l[i-1])]+1 if mat[i][(mat[0][j] - l[i-1])]+1 < mat[i-1][j] else mat[i-1][j]
for i in mat:
    print(i)
print(mat[len(l)][num])'''
l = [3,4]
num = 10
l1 = [-1]*(num+1)
l1[0] = 0
for i in l:
    for j in range(1,num+1):
        if j >= i:
            if l1[j-i]!=-1:
                if l1[j]!=-1:
                    l1[j] = min(l1[j],l1[j-i]+1)
                else:
                    l1[j] = l1[j-i]+1
print(l1[-1])
    