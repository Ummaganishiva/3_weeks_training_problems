def checkpalindrome(st):
    return st == st[::-1]
s = "abdghgdhj"
ma = 0
c = 0
l = []
for i in range(len(s)-1):
    for j in range(len(s)-1,i,-1):
        if s[i] == s[j]:
            if checkpalindrome(s[i:j+1]):
                c = j-i 
                if c > ma:
                    ma = c
                    l.append(s[i:j+1])
print(l)