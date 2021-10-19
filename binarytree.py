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

    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements

    def pre_order(self):
        elements = []
        
        elements.append(self.data)
         
        if self.left:
            elements += self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        return elements

    def post_order(self):
        elements = []

        if self.left:
            elements += self.left.post_order()
        if self.right:
            elements += self.right.post_order()
        
        elements.append(self.data)

        return elements


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