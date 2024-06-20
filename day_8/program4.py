def fun(mat,i,j):
    if mat[i][j] == 0:
        return 
    else:
        mat[i][j] = 0
    if i+1<n:
        fun(mat,i+1,j)
    if i-1>=0:
        fun(mat,i-1,j)
    if j+1<n:
        fun(mat,i,j+1)
    if j-1>=0:
        fun(mat,i,j-1)
    return 
n = int(input())
mat = []
c = 0
for i in range(n):
    mat.append(list(map(int,input().split())))
row,col = map(int,input().split())
fun(mat,row-1,col-1)
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            c=c+1
print(c)