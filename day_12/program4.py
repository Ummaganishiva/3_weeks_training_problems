'''
n = 5
mat = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
row = []
col = []
column = []
def fun(mat,i,j,c):
    if c == n:
        return mat 
    if i == n:
        return mat 
    if j == n:
        mat[row[-1]][col[-1]] = 0
        k = row[-1]
        for j in range(col[-1],n):
            column.remove((k,j))
            k = k+1
        k = row[-1]
        for j in range(col[-1]-1,-1,-1):
            if k < n :
                column.append((k,j))
            k = k+1
        row.pop()
        col.pop()
        
    if i not in row and j not in col and (i,j) not in column:
        row.append(i)
        col.append(j)
        mat[i][j] = 1
        k = i
        for j in range(j,n):
            if k < n :
                column.append((k,j))
            k = k+1
        k = i
        for j in range(j-1,-1,-1):
            if k < n :
                column.append((k,j))
            k = k+1
        c = c+1
        i = i+1
        j = 0
    else:
        j = j+1
    return fun(mat,i,j,c)
print(fun(mat,0,0,0))
'''
'''
n = 4
mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def canweplace(mat,i,j):
        flag = 0
        for i in range(i,n):
            if mat[i][j] == 1:
                flag = 1
        for j in range(j,n):
            if mat[i][j] == 1:
                flag = 1
        for i in range(i,-1,-1):
            if j >= 0:
                if mat[i][j] == 1:
                    flag = 1
            j = j-1
        for i in range(i,-1,-1):
            if j <= n:
                if mat[i][j] == 1:
                    flag = 1
            j = j+1
        if flag == 1:
            return False 
        else:
            return True
def fun(mat,i,j):
    if i == n:
        return mat 
    if j == n:
        i = i-1
        return mat
    if canweplace(mat,i,j):
        mat[i][j] = 1
        i = i+1
        j = 0
    else:
        j = j+1
    mat = fun(mat,i,j)
    return mat
print(fun(mat,0,0))
'''
def safe(i,j):
    if i == u:
        return 0
    if j == v:
        return 0
    r = i
    c = j
    for i in range(r+1):
        if mat[i][c] == 1:
            return 0
    while (r>=0 and c>=0):
        if mat[r][c] == 1:
            return 0
        r = r-1
        c = c-1
    r = i
    c = j
    while (r>=0 and c<n):
        if mat[r][c] == 1:
            return 0
        r = r-1
        c = c+1
    return 1
def queen(i):
    if i == n:
        return mat
    if i!=u:
        for j in range(n):
            if safe(i,j):
                mat[i][j] = 1
                return queen(i+1)
            mat[i][j] = 0
        return queen(i+1)
    else:
        return queen(i+1)
    
n = 5
u = 1
v = 3
mat = [[0]*n for i in range(n)]
res = queen(0)
for i in res:
    print(i)