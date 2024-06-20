n = 5
mat = [
    [0,1,0,0,1],
    [1,0,0,1,1],
    [0,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,1]
]
def recursion(mat,i,j,c):
    if mat[i][j] == 0:
        return c
    else:
        mat[i][j] = 0
        c=c+1
    if i+1<n:
        c = recursion(mat,i+1,j,c)
    if i-1>=0:
        c = recursion(mat,i-1,j,c)
    if j+1<n:
        c = recursion(mat,i,j+1,c)
    if j-1>=0:
        c = recursion(mat,i,j-1,c)
    return c
        

def fun(mat):
    ma = 0
    count = 0
    co =0
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                co = recursion(mat,i,j,0)
                print(co)
                count = count+1
            if co > ma:
                ma = co
    return count,ma
count,ma = fun(mat)
print("total islands = ",count)
print("Highest acres = ",ma)