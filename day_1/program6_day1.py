st = list(map(float,input().split()))
even=0
odd=0
f=0
for i in st:
    if i%2 == 0:
        even=even+i
    elif i%2 == 1.0:
        odd = odd+i
    else:
        f=f+i
print("even - ",int(even))
print("odd - ",int(odd))
print("float - ",f)
        
        
        

