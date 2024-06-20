n = 143492
s = list(str(n))
if str(n) == str(n)[::-1]:
    print(n)
else:
    if len(s)%2!=0:
        mid = len(s)//2
        i = 0
        j = len(s)-1
        while j!=i:
            if int(s[j])>int(s[i]):
                s[j] = s[i]
                s[j-1] = str(int(s[j-1])+1)
                i = i+1
                j = j-1
            elif int(s[j])<int(s[i]):
                s[j] = s[i]
                i = i+1
                j = j-1
            else:
                i = i+1
                j = j-1
    else:
        i = 0
        j = len(s)-1
        while j>i:
            if i == j-1:
                if int(s[i]<s[j]):
                    s[i] = str(int(s[i])+1)
                    s[j] = s[i]
                else:
                    s[j] = s[i]
                j = j-1
                i = i+1
            else:
                if int(s[j])>int(s[i]):
                    s[j] = s[i]
                    s[j-1] = str(int(s[j-1])+1)
                    i = i+1
                    j = j-1
                elif int(s[j])<int(s[i]):
                    s[j] = s[i]
                    i = i+1
                    j = j-1
                else:
                    i = i+1
                    j = j-1
            
        print("".join(s))