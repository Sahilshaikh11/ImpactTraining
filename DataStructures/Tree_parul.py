#!/usr/bin/env python
# coding: utf-8

# In[14]:


# trees
'''

Types of Binary Tree based on the number of children:
Following are the types of Binary Tree based on the number of children:

Full Binary Tree
Degenerate Binary Tree
Skewed Binary Trees


Types of Binary Tree On the basis of the completion of levels:
Complete Binary Tree
Perfect Binary Tree
Balanced Binary Tree

Some Special Types of Trees:
On the basis of node values, the Binary Tree can be classified 
into the following special types:

Binary Search Tree
AVL Tree
Red Black Tree
B Tree
B+ Tree
Segment Tree
'''
class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
def insert(root,data):# root.left
        if  root is None:
            print("hello")
            root=node(data) # node = 4
            return root
        elif data>root.data:# root.data=23
            print("hi")
            root.right= insert(root.right,data)
        elif data<root.data:
            print("morning")
            root.left=insert(root.left,data)# root=None
        return root
   
    def search(self, root, target):
        if root is None:
            return -1
        if root.data==target:
            return root.data
        elif root.data>target:
            self.search(root.left,target)
        else:
            self.search(root.right,target)
        return -1
T1=Tree()
insert(T1.root,23)
insert(T1.root,4)
insert(T1.root,34)
insert(T1.root,1)
insert(T1.root,5)
insert(T1.root,20)
showTree(T1.root)
#23 4 34 1 5 20
        
    
    
    
    
    
    
    
    
    
    
    
    
    


# In[7]:


# binary search tree

class node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None


def insert(root, data):
    
    if  root is None:
        root = node(data)
        return root
    if data < root.data:
        root.l = insert(root.l, data)
    else:
        root.r = insert(root.r, data)
    return root


def display(root):
    if root:
        display(root.l)
        print(root.data, end=" ")
        display(root.r)


r = node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

display(r)


# In[4]:


def BST_search(self, find_key):
      if self.key == find_key:    
        print("The node is present")
        return
      if find_key < self.key:   
        if self.l:   
            self.l.BST_search(find_key)
        else:
          print("Empty Node")
      else:
        if self.r:
            self.r.BST_search(find_key) 
            return true
        else:   
            print("Empty Node")  


# In[13]:


# calculates the inorder successor of the Node 
def Inorder_Successor(node):
    current = node
    while(current.l is not None):
        current = current.l

    return current


def remove_key(root, key):
    if  root is None:
        return root
    if key < root.key:
        root.l = remove_key(root.l, key)
    elif(key > root.key):
        root.h = remove_key(root.h, key)
    else:
        if root.l is None:
            temp = root.r
            root = None
            return temp

        elif root.r is None:
            temp = root.l
            root = None
            return temp
        temp = Inorder_Successor(root.r)
        root.key = temp.key
        root.r = remove_key(root.r, temp.key)

    return root


# In[14]:


# avl tree
# AVL tree implementation in Python


import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)


# In[ ]:




