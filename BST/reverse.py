class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return Node(val)
        if root.data > val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)
    def takecount(self,root,count,k):
        if root:
            count = self.takecount(root.left,count,k)
            count += 1
            if count == k:
                print(root.data,end="")
            count = self.takecount(root.right,count,k)
        return count
    def delete(self,root,val):
        if val > root.data:
            root.right = self.delete(root.right,val)
        elif val < root.data:
            root.left = self.delete(root.left,val)
        else:
            if root.right == None:
                return root.left
            elif root.left == None:
                return root.right
            else:
                root.data = self.minvalue(root.right)
                root = self.delete(root.right,root.data)   
        return root
    def findclose(self,root,key):
        if root.data<key
        if root:
            close = self.findclose(root.left,key)
    def minvalue(root):
        minv = 0
        while root != None:
            root = root.left
            minv = root.data
        return minv
    

   
a = BST()
a.root = a.insert(a.root, 50)
a.root = a.insert(a.root, 30)
a.root = a.insert(a.root, 20)
a.root = a.insert(a.root, 10)
a.root = a.insert(a.root, 40)
a.root = a.insert(a.root, 80)
a.root = a.insert(a.root, 70)

# a.takecount(a.root,0,6)
a.delete(a.root,70)
a.inorder(a.root)


