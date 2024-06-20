di = {5: [(7, 4), (3, 2)], 7: [(5, 4), (4, 2), (3, 3)],
     4: [(7, 2), (8, 4), (2, 1)], 3: [(5, 2), (7, 3), (8, 7)],
     8: [(3, 7), (4, 4), (2, 2)], 2: [(4, 1), (8, 2)]}


'''
di = {
    5:[7,3],
    7:[3,4,5],
    3:[5,7,8],
    4:[7,8,2],
    8:[3,4,2],
    2:[4,8]
}
'''
'''
di = {
    5:[(7,2),(3,5)],
    7:[(3,4),(4,6),(5,2)],
    3:[(5,5),(7,4),(8,2)],
    4:[(7,6),(8,4),(2,2)],
    8:[(3,2),(4,4),(2,5)],
    2:[(4,2),(8,5)]
}
'''
def findallpathswithcosts(t,num,start,end,l,cost):
    l.append(num)
    cost = cost+t[1]
    if num == end:
        print(l,"cost = ",cost)
        l.pop()
        cost = cost-num
        return 
    for i in di[num]:
        if i[0] not in l:
            findallpathswithcosts(i,i[0],start,end,l,cost)
    l.pop()
    cost = cost-num
def findminpathwithcosts(t,num,start,end,l,cost,m,res):
    l.append(num)
    #print(l)
    cost = cost+t[1]
    if num == end:
        print(l,"cost = ",cost)
        if cost < m:
            m = cost
            res = l.copy()
        l.pop()
        cost = cost-num
        return m,res
    for i in di[num]:
        if i[0] not in l:
            m,res = findminpathwithcosts(i,i[0],start,end,l,cost,m,res)
    l.pop()
    cost = cost-num
    return m,res
def printallpathsfromallelements(start):
    l1 = fun(start,[])
    for i in range(1,len(l1)):
        findallpathswithcosts((5,0),start,start,l1[i],[],0)
    

def fun(num,l):
    l.append(num)
    for i in di[num]:
        if i not in l:
            fun(i,l)    
    return l
            
def findallpaths(start,end,l):
    l.append(start)
    if start == end:
        print(l)
        l.pop()
        return 
    for i in di[start]:
        if i not in l:
            findallpaths(i,end,l)
    l.pop()
#print(findminpathwithcosts((5,0),5,5,2,[],0,100000,[]))
#printallpathsfromallelements(5)
findallpathswithcosts((5,0),5,5,2,[],0)
#print(res)
#fun(5,[])