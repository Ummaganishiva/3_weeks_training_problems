class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class tree:
    def __init__(self):
        self.root = None
    def create(self,root,x):
        if root == None:
            root = node(x)
        elif x<root.data:
            root.left = self.create(root.left,x)
        else:
            root.right = self.create(root.right,x)
        return root
    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data,end = " ")
            self.inorder(temp.right)
    def preorder(self,root):
        if root == None:
            return
        print(root.data,end = " ")
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end = " ")
    def addnodes(self,temp):
        if temp == None:
            return 0
        return temp.data + self.addnodes(temp.left) + self.addnodes(temp.right)
    def addeven(self,temp):
        if temp == None:
            return 0
        if temp.data%2 == 0:
            return temp.data + self.addeven(temp.left) + self.addeven(temp.right)
        else:
            return self.addeven(temp.left) + self.addeven(temp.right)
    def addodd(self,temp):
        if temp == None:
            return 0
        if temp.data%2 != 0:
            return temp.data + self.addodd(temp.left) + self.addodd(temp.right)
        else:
            return self.addodd(temp.left) + self.addodd(temp.right)
    def evenodd_diff(self,temp):
        if temp == None:
            return 0 
        if temp.data%2 == 0:
            return temp.data + self.evenodd_diff(temp.left) + self.evenodd_diff(temp.right)
        return self.evenodd_diff(temp.left) + self.evenodd_diff(temp.right) - temp.data
    def findheight(self,temp):
        if temp == None:
            return -1
        return 1 + max(self.findheight(temp.left) , self.findheight(temp.right))
    def checkbalance(self,temp):
        if temp == None:
            return -1
        return abs(self.checkbalance(temp.left) - self.checkbalance(temp.right)) <=1
    def count_leaf_nodes(self,temp,c):
        if temp == None:
            return 0
        if temp.left == None and temp.right == None:
            c = c+1
            return c 
        return self.count_leaf_nodes(temp.left,c) + self.count_leaf_nodes(temp.right,c)
    def count_leaf_nodes_sum(self,temp,tot):
        if temp == None:
            return 0
        if temp.left == None and temp.right == None:
            tot = tot+temp.data
            return tot 
        return self.count_leaf_nodes_sum(temp.left,tot) + self.count_leaf_nodes_sum(temp.right,tot)
    def search(self,temp,target):
        if temp == None:
            return False
        if temp.data == target:
            return True 
        elif target < temp.data:
            self.search(temp.left,target)
        else:
            self.search(temp.right,target)
    def find_depth(self,temp,x,c):
        if temp == None:
            return -1
        if temp.data == x:
            return c
        if x < root.data:
            return self.find_depth(temp.left,x,c+1)
        else:
            return self.find_depth(temp.right,x,c+1)
    def leftview(self,temp,c,di):
        if temp == None:
            return 
        if c not in di:
            di.append(c) 
            print(temp.data,end = " ")
        self.leftview(temp.left,c+1,di)
        self.leftview(temp.right,c+1,di)
    def righttview(self,temp,c,di):
        if temp == None:
            return 
        if c not in di:
            di.append(c) 
            print(temp.data,end = " ")
        self.righttview(temp.right,c+1,di)
        self.righttview(temp.left,c+1,di)
    def topview(self,temp,c,di,l):
        if temp:
            l.append((temp,c))
        while len(l)!=0:
            if l[0][1] not in di:
                di[l[0][1]] = l[0][0].data
            if l[0][0].left:
                l.append((l[0][0].left,l[0][1]-1))
            if l[0][0].right:
                l.append((l[0][0].right,l[0][1]+1))
            l.pop(0)
        res = sorted(di)
        for i in res:
            print(di[i],end = " ")
    def bottomview(self,temp,c,di,l):
        if temp:
            l.append((temp,c))
        while len(l)!=0:
            if (l[0][1] not in di) or (l[0][1] in di):
                di[l[0][1]] = l[0][0].data
            if l[0][0].left:
                l.append((l[0][0].left,l[0][1]-1))
            if l[0][0].right:
                l.append((l[0][0].right,l[0][1]+1))
            l.pop(0)
        res = sorted(di)
        for i in res:
            print(di[i],end = " ")
t1 = tree()
t1.root = t1.create(t1.root,23)
t1.root = t1.create(t1.root,22)
t1.root = t1.create(t1.root,30)
t1.root = t1.create(t1.root,21)
t1.root = t1.create(t1.root,24)
t1.root = t1.create(t1.root,33)
t1.root = t1.create(t1.root,29)

t1.root = t1.create(t1.root,12)
t1.root = t1.create(t1.root,27)
t1.root = t1.create(t1.root,59)
t1.root = t1.create(t1.root,60)
t1.root = t1.create(t1.root,57)
'''

t1.inorder(t1.root)
print()
print(t1.addnodes(t1.root))
print()
print(t1.addeven(t1.root))
print()
print(t1.addodd(t1.root))
print()
print(t1.evenodd_diff(t1.root))
print()
print(t1.findheight(t1.root))
print()
print(t1.checkbalance(t1.root))
print(t1.count_leaf_nodes(t1.root,0))
print(t1.count_leaf_nodes_sum(t1.root,0))
'''
t1.leftview(t1.root,0,[])
print()
t1.righttview(t1.root,0,[])
print()
t1.topview(t1.root,0,{},[])
print()
t1.bottomview(t1.root,0,{},[])