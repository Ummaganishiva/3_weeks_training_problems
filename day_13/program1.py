'''n = int(input())
new = []
for i in range(n):
    l = list(map(str,input().split()))
    if l[0] == '1':
        if l not in new:
            new.append(l)
    elif l[0] == '2':
        for i in new:
            if l[1] == i[1]:
                print(True)
                break
        else:
            print(False)
    elif l[0] == '3':
        c = 0
        length = len(l[1])
        for i in new:
            if l[1] == i[1][:length]:
                c = c+1
                #print(True)
        print(c)
        #else:
            #print(False)'''

#using oops
class oops:
    def add(self,word,new):
        new.append(word)
    def search(self,word,new):
        if word in new:
            print(True)
        else:
            print(False)
    def count(self,word,new):
        self.c = 0
        self.length = len(word)
        for i in new:
            if word == i[:self.length]:
                self.c = self.c+1
        print(self.c)
        
        
obj = oops()
n = int(input())
new = []
for i in range(n):
    num,word = map(str,input().split())
    if num == '1':
        if word not in new:
            obj.add(word,new)
    elif num == '2':
        obj.search(word,new)
    elif num == '3':
        obj.count(word,new)