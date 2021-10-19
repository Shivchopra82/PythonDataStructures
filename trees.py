from typing import no_type_check_decorator


# 1.Trees is the datastructure used to show the hierarchy in the elements.
# 2.Nodes in the tree contain some other elements as their child nodes. 
# 3.Nodes in the tree are classified according to the level.
# 4.Node in the zeroth level is consider as root node. 
# 5.Node in the last level is considered as child nodes they don't have their own childs. 
# 6. A node with child nodes are called as ancestor for child nodes. 
# 7. Suppose a node is on n level, then all the nodes with level greater than n are called descendents of that nodes. 

#  ============================================================================================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []   #This will contain list of all the childrens of that node (every child is also a treenode)
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def level(self):            #This function counts the level of the given node.
        level = 0             #We do counting of ancestors.
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.level() * 3 
        if self.parent:
            indent = spaces + "---| "
        else:
            indent = spaces
        print(indent + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()  




root = Node("Fashion")

summer = Node("Summer")
summer.add_child(Node("Shorts"))
summer.add_child(Node("Tshirts"))
summer.add_child(Node("Flipslops"))

winter = Node("Winter")
winter.add_child(Node("Jeans"))
winter.add_child(Node("Shirts"))
winter.add_child(Node("Shoes"))

rainy = Node("Rainy")
rainy.add_child(Node("Raincoats"))
rainy.add_child(Node("Gumboots"))
rainy.add_child(Node("Gloves"))

root.add_child(summer)
root.add_child(winter)
root.add_child(rainy)

root.print_tree()
