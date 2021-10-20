# 1. For the internal implementation of sets in python we can use binary search tree. 
# 2. In binary search tree every node has maximum of two child nodes. 
# 3. Binary search tree is a special case of binary tree.
# 4. All the nodes on left side of particular node has value less than that particular node.
# 5. All the nodes on right side of the particular node has value greater than particular node.
# 6. No node is repeated. 

# Binary search tree makes searching of particular node is made more efficient.
# Every iteration of search reduces the number of elements by half.
# Search complexity O(logn). 
# Insert complexity O(logn).


                        # SEARCHING IN BINARY SEARCH TREE

# 1. BFS (breadth first search)

# 2. DFS (depth first search)
#    - Inorder traversal     L root R
#    - Pre order traversal   root L R
#    - Post order traversal  L R root

from typing import no_type_check_decorator


class bst_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst_node(data)
        
        else :
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst_node(data)

# Add child method is used to add new node in the binary search tree. 

    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements

# In order prints the elements of binary search tree in left root right format. 

    def pre_order(self):
        elements = []
        
        elements.append(self.data)
         
        if self.left:
            elements += self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        return elements

# Pre order prints the elements of the binary search tree in root left right format. 

    def post_order(self):
        elements = []

        if self.left:
            elements += self.left.post_order()
        if self.right:
            elements += self.right.post_order()
        
        elements.append(self.data)

        return elements

# Post order prints the elements of the binary search tree in left right root format. 

    def search(self, key):
        if self.data == key:
            return True

        if key < self.data:
            if self.left:
                return self.left.search(key)
            else:
                return False

        if key > self.data:
            if self.right:
                return self.right.search(key)
            else:
                return False

# Search method is used to find out that the particular node exist in binary search tree or not. It only returns the bool value. 

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

# This function will return minimum of all the nodes in the tree.

    def max(self):
        if  self.right is None:
            return self.data
        return self.right.max()

# This function will return the maximun of all the nodes in the tree.

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right

            minval = self.right.min()
            self.data = minval
            self.right = self.right.delete(minval)

        return self

# The delete function is used to delete the particular node from the tree.

list = [55,6,4,9,22,5,6,4,8,9,55,44,88,99,77,66,33,22,11,20,30,40,50,60,70,80,90,100]
root1 = bst_node(list[0])
for i in range(len(list)):
    root1.add_child(list[i])


pre = [1,2,3,4,5,6,7,8,9]
root2 = bst_node(pre[4])
for i in range(len(pre)):
    root2.add_child(pre[i])
print(root1.pre_order())
print(root2.pre_order())
print(root1.post_order())
print(root2.post_order())
print(root1.in_order())    
print(root2.in_order())    
print(root2.search(7))  
root1.delete(6)
root2.delete(6)
print(root1.in_order())
print(root2.in_order())