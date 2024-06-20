class node:
    def __init__(self,u):
        self.data = u 
        self.next = None 
class sll:
    def __init__(self):
        self.head = None
    def display(self):
        t = self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addback(self,data):
        if self.head == None:
            self.head = node(data)
        else:
            t = self.head
            while(t.next!=None):
                t=t.next
            t.next = node(data)
    def addfront(self,data):
        new = node(data)
        new.next = self.head 
        self.head = new
    def search(self,target):
        t = self.head
        while(t!=None):
            if t.data == target:
                print("Element found")
                break
            t = t.next
        else: 
            print("Element Not found")
    def findmiddle(self):
        slow = self.head
        fast = self.head
        while (fast!=None and fast.next!=None):
            slow = slow.next 
            fast = fast.next.next
        print("Middle element ",slow.data)
    def checklength(self):
        fast = self.head
        while (fast!=None and fast.next!=None):
            fast = fast.next.next
        if fast == None:
            print("Even")
        else:
            print("Odd")
    def evensum(self):
        t = self.head
        s = 0 
        while(t!=None):
            if (t.data)%2 == 0:
                s=s+t.data
            t=t.next
        print("sum = ",s)
    def longestsubsequence(self):
        t = self.head 
        c = 1
        ma = 0
        while (t.next!=None):
            if t.next.data == t.data+1:
                c = c+1
            else:
                if c > ma:
                    ma = c
                c = 1
            t = t.next
        if c>ma:
            ma = c
        print("Longest sub sequence is ",ma)
    def bubblesort(self):
        t = self.head
        length = 0
        while t!=None:
            length = length+1
            t=t.next
            f = 0
        for i in range(length-1):
            t = self.head
            for j in range(length-i-1):
                if t.data > t.next.data:
                    f = 1
                    t.data,t.next.data = t.next.data,t.data
                t = t.next
            if f == 0:
                break
        ''' 
        Another program
        t = self.head
        while t.next!=None:
            t1 = t.next
            while t1.next!=None:
                if t1.data > t1.next.data:
                    t.data,t.next.data = t.next.data,t.data
                t1 = t1.next
            t = t.next
        '''
    def findpairs(self):
        t = self.head
        while t.next!=None:
            t1 = t.next
            while t1!=None:
                print(t.data,t1.data)
                t1 = t1.next
            t = t.next
    def reverse(self):
        prev = None 
        cur = self.head 
        temp = cur
        #later = cur.next
        while cur!=None:
            temp = cur.n
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev
            
        
a = sll()
b = sll()
#a.addback(10)
a.addback(40)
a.addback(20)
a.addback(19)
a.addback(50)
a.addback(60)
a.addback(61)
a.addback(62)
a.addback(63)
a.addback(64)
'''
a.addback(65)
a.addback(43)
a.addfront(3)
a.addfront(2)
a.addfront(1)
a.display()
a.evensum()
a.search(50)
a.findmiddle()
a.checklength()
a.longestsubsequence()
a.findpairs()
a.bubblesort()'''
a.display()
a.reverse()
print()
a.display()
'''
print()
b.addback(100)
b.addback(200)
b.addback(300)
b.addback(400)
b.display()
b.evensum()'''