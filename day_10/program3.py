'''
#given two lists in which even number in first list is added with every odd number in second list and appended to a resultant list
elist = [6,3,2,9,4,7]
olist = [8,7,5,3,6,9]
n = len(elist)
def fun(elist,olist,res,n,i,j):
    if i == n:
        return res
    if j == n:
        i = i+1 
        j = 0
    if elist[i]%2!=0:
        i = i+1 
    else:
        if olist[j]%2 != 0:
            res.append(elist[i]+olist[j])
        j = j+1 
    return fun(elist,olist,res,n,i,j)

print(fun(elist,olist,[],n,0,0))
'''
#printing sums of all numbers that are added from one even to all odd numbers, like that all even numbers from list 1
elist = [6,3,2,9,4,7]
olist = [8,7,5,3,6,9]
n = len(elist)
def fun(elist,olist,res,n,i,j,s):
    if i == n:
        return res
    if j == n:
        i = i+1 
        j = 0
        res.append(s)
        s = 0
    if elist[i]%2!=0:
        i = i+1 
    else:
        if olist[j]%2 != 0:
            s = s+(elist[i]+olist[j])
            #res.append(elist[i]+olist[j])
        j = j+1 
    return fun(elist,olist,res,n,i,j,s)

print(fun(elist,olist,[],n,0,0,0))