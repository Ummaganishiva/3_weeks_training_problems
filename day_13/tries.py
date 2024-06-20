class node:
    def __init__(self):
        self.di = {}
        self.flag = 0
        self.count = 1
class trie:
    def __init__(self):
        self.root = node()
    def add(self,st):
        temp = self.root
        for i in st:
            if i not in temp.di:
                temp.di[i] = node()
            temp.count = temp.count+1
            temp = temp.di[i]
            
        temp.flag = 1
    def searchword(self,str):
        temp = self.root
        for i in str:
            if i in temp.di:
                temp = temp.di[i]
            else:
                return "Not Found"
        if temp.flag == 1:
            return "Found"
        else:
            return "Not Found"
    def searchprefix(self,word):
        temp = self.root
        self.f = 0
        for i in word:
            if i in temp.di:
                temp = temp.di[i]
            else:
                self.f = 1
                break 
        if self.f == 1:
            print("Not Found")
        else:
            print("Found")
    def find_word_with_prefix(self,word):
        def dfs(temp,s):
            if temp.flag == 1:
                print(s)
            for i in temp.di:
                dfs(temp.di[i],s+i)
        temp = self.root
        s = ""
        for i in word:
            if i in temp.di:
                s = s+i
                temp = temp.di[i]
            else:
                return 
        dfs(temp,s)
    def find_longest_word_with_prefix(self,l1):
        def dfs(temp,s,l):
            if temp.flag == 1:
                self.l.append(s)
            for i in temp.di:
                dfs(temp.di[i],s+i,l)
        def findwords(str):
            temp = self.root
            s = str
            for i in str:
                if i in temp.di:
                    temp = temp.di[i]
                else:
                    return 
            dfs(temp,s,self.l)
        self.l = []
        for i in l1:
            findwords(i)
        ma = 0
        new = []
        self.l.sort()
        print(self.l)
        for i in self.l:
            if len(i)>ma:
                ma = len(i)
                word = i
        print(word)
                
obj = trie()
obj.add('world')
obj.add("words")
obj.add("apple")
obj.add("word")
obj.add("ape")
#print(obj.searchword("woodsjhf"))
#obj.searchprefix("woo")
#obj.find_word_with_prefix("wor")
obj.find_longest_word_with_prefix(['b','ba','ap','wo'])
