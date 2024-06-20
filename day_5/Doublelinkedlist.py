class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data,end = "->")
            temp = temp.next 
        print()
    def rev_display(self):
        temp = self.tail
        while temp!=None:
            print(temp.data,end = "->")
            temp = temp.prev 
        print()
    def addback(self,val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            t = node(val)
            self.tail.next = t
            t.prev = self.tail
            self.tail = self.tail.next 
    def addfront(self,val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            t = node(val)
            t.next = self.head
            self.head.prev = t 
            self.head = t   
    def search(self,target):
        temp1 = self.head
        temp2 = self.tail
        while temp1!=temp2 and temp1!=temp2.next:
            if temp1.data == target or temp2.data == target:
                print("Element Found")
                break
            temp1 = temp1.next
            temp2 = temp2.prev
        if temp1.data == target:
            print("Element Found")
        else:
            print("Element not found")
    def checklength(self):
        temp1 = self.head
        temp2 = self.tail
        while temp1!=temp2 and temp1!=temp2.next:
            temp1 = temp1.next
            temp2 = temp2.prev     
        if temp1 == temp2.next:
            print("Even")
        else:
            print("Odd")       
    def checkpalindrome(self):
        temp1 = self.head
        temp2 = self.tail
        while temp1!=temp2 and temp1!=temp2.next:
            if temp1.data !=temp2.data:
                print("Not a Palindrome")
                break
            temp1 = temp1.next
            temp2 = temp2.prev
        else:
            print("Palindrome")
    def transfer(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next 
        temp = slow.prev
        slow.prev = None
        self.tail.next = self.head
        self.head = slow
        temp.next = None
        self.tail = temp
    def reverseadjacent(self):
        t1 = self.head
        t2 = self.head.next
        temp = self.head
        self.head = self.head.next
        pre = None
        while temp!=None:
            temp = t2.next
            t2.next = t1
            t1.prev = t2
            t2.prev = pre
            if pre:
                pre.next = t2
            pre = t1
            if temp:
                t1 = temp 
                t2 = temp.next
        self.tail = pre
        self.tail.next = None
    def balanced_paranthesis(self):
        stack = []
        temp = self.head
        c = 0
        f = 0
        while temp!=None:
            if temp.data in  "[{(":
                stack.append(temp.data)
                c = c+1
            else:
                if len(stack)>0 and ((temp.data == ')' and stack[-1] == '(') or (temp.data == '}' and stack[-1] == '{') or (temp.data == ']' and stack[-1] == '[')):
                    c =c+1
                    stack.pop()
                else:
                    f = 1
                    c =c+1
                    break 
            temp = temp.next
        if f==1 or len(stack)>0:
            print("position = ",c)
        else:
            print("-1")
    def even_odd_diff(self):
        temp = self.head
        def fun(temp,a,b):
        #print(temp.data)
            if temp == None:
                return abs(a-b)
            if temp.data%2 == 0:
                return fun(temp.next,a+temp.data,b)
            else:
                return fun(temp.next,a,b+temp.data)
        return fun(temp,0,0)
    def count_primes(self):
        def fun(tem,c):
            if tem ==  None:
                return c
            def prime(n,i):
                if n == 1:
                    return False
                if n%i == 0:
                    return False
                if i>=n//2:
                    return True
                return prime(n,i+1)
                
            if prime(tem.data,2):
                return fun(tem.next,c+1)
            else:
                return fun(tem.next,c)
        return fun(self.head,0)
            
            
x = dll()
'''(({{[[]]}}){{'''
'''
x.addfront(10)
x.addfront(20)
'''
x.addback(1)
x.addback(4)
x.addback(3)
#x.addfront(2)
#x.addfront(9)
#x.addback(22)
x.addback(10)
x.addback(5)
x.addback(7)
x.addback(12)
'''
x.addback(']')
x.addback('}')
x.addback('}')
x.addback(')')
x.addback('{')
x.addback('{')
'''
print(x.count_primes())
#print(x.even_odd_diff())
#x.addback(30)
#x.display()
#x.transfer()
#x.display()
#x.reverseadjacent()
#x.display()
#x.balanced_paranthesis()
#x.search(22)
#x.checklength()
#x.checkpalindrome()