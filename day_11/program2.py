
'''
input = "abcd"
def fun(input,res):
    if len(input) == 0:
        print(res,end = " ")
        return
    fun(input[1:],res+input[0])
    fun(input[1:],res)
fun(input,"")
'''
str1 = "abcd"
str2 = "axbd"
s = ""
mat = [[0]*(len(str2)+1) for i in range(len(str1)+1)]
print(mat)
for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
            mat[i][j] = mat[i-1][j-1] + 1
        else:
            mat[i][j] = max(mat[i-1][j],mat[i][j-1])
print(mat[len(str1)][len(str2)])
i = len(str1)
j = len(str2)
while i>0:
    while j>0:
        if str1[i-1] == str2[j-1]:
            s = s+str1[i-1]
            i = i-1
            j = j-1
        else:
            if mat[i][j] == mat[i-1][j]:
                i = i-1
            else:
                j = j-1
print(s[::-1])