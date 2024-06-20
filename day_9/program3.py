s = list(map(str,input().split(',')))
st = ""
for i in s:
    l = list(i.split(':'))
    for j in range(len(l[0]),0,-1):
        if str(j) in l[1]:
            st = st+l[0][j-1]
            break
    else:
        st = st+'x'
    
print(st)