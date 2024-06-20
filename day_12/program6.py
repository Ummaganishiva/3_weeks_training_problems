l = [2,3,5,6]
num = 6
n = len(l)
mat = [[0]*(num+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(num+1):
        if i == 0:
            mat[i][j] = 0
        elif l[i-1] <= j:
            if j - l[i-1] == 0:
                mat[i][j] = 1
            elif mat[i-1][j - l[i-1]]!=0:
                mat[i][j]=  mat[i-1][j - l[i-1]]+1
            else:
                mat[i][j] = mat[i-1][j]
        else:
            mat[i][j] = mat[i-1][j]
for i in mat:
    print(i)
print(mat[-1][-1])