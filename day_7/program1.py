'''
l = list(map(int,input().split()))
n = len(l)
result = []
def fun(l,i,j,k,n,res):
    if i == n-2 and j == n-1 and k == n:
        return res 
    elif j == n-1:
        i = i+1
        j = i+1
        k = j+1
    elif k == n:
        j = j+1
        k = j+1
    else:
        res.append([l[i],l[j],l[k]])
        k = k+1
    return fun(l,i,j,k,n,res)
print(fun(l,0,1,2,n,result))
'''

'''
# printing any number of combinations from a list

def combinations(l,k):
    def fun(curr,start):
        if len(cur) == k:
            print(curr)
            return
        for i in range(start.len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun(l,0)
a = lis(map(int,input().split()))
k = int(input())
combinations(a,k)
'''
    