'''
def fun(mat,i,j,si):
    if si == len(s):
        return True
    if i == n:
        return False
    if mat[i][j] == s[si]:
        si=si+1
        if si == len(s):
            return True
        if i+1<n and mat[i+1][j] == s[si]:
            i = i+1
        elif i-1>=0 and mat[i-1][j] == s[si]:
            i = i-1
        elif j+1<n and mat[i][j+1] == s[si]:
            j = j+1
        elif j-1>=0 and mat[i][j-1] == s[si]:
            j = j-1
        else:
            si = 0
            j = j+1
            if j>=n:
                i = i+1
                j = 0
    else:
        j = j+1
        if j>=n:
            i = i+1
            j = 0
    return fun(mat,i,j,si)
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(str,input().split())))
s = input()
print(fun(mat,0,0,0))
'''