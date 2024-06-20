s = list(input())
'''
for i in range(len(s)):
    if s[i] == '*':
        s[i] = '#'
        j = i-1
        while s[j]=='#':
            j=j-1
            continue
        s[j] = '#'
for i in range(len(s)):
    if s[i]!='#':
        print(s[i],end="")
'''
stack = []
for i in range(len(s)):
    if s[i] == '*':
        stack.pop()
    else:
        stack.append(s[i])
print("".join(stack))
    
s = list(map(str,input().split()))
ans = ['0']*len(s)
for i in range(len(s)):
    index = int(s[i][-1])
    ans[index-1] = s[i][:len(s[i])-1]
print(' '.join(ans))
