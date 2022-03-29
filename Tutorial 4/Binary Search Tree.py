#Define a node class that has left and  right sides
class Node:
    def __init__(self, Node_value):
        self.left = None    # left side node (leaf)
        self.right = None   #right side node (leaf)
        self.Node_value = Node_value   # actual node value
 #Define a function to insert Node_value in to the tree
    def insert(self, Node_value):
# Compare the new value with the parent node
        if self.Node_value:   # if there is a root node      
            if Node_value < self.Node_value:  # if the value that we need to insert is less than root value
                if self.left is None:     # if no left side node exist
                    self.left = Node(Node_value) # create a left side node
                else:                      # otherwise (means there is an empty left node)
                    self.left.insert(Node_value)  # put that value in the left of the existing node
            elif Node_value > self.Node_value:          # do the same thing for the right side node if >    
                if self.right is None:
                    self.right = Node(Node_value)
                else:
                    self.right.insert(Node_value)
        else:        # if no root exists
            self.Node_value = Node_value     # put the value in the root

# Printing the binary tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.Node_value),
        if self.right:
            self.right.PrintTree()

#search
def search(root,target,count):
    #if the value of the node is equal to target
    if root.Node_value == target:
        print(str(count)," step to search the target")
    elif root.Node_value > target:
        if root.left:
            search(root.left,target,count+1)
        #root.left is none which means that the target does not exist
        else:
            print(str(target)," does not exist")
    else:
        if root.right:
            search(root.right,target,count+1)
        #root.right is none which means that the target does not exist
        else:
            print(str(target)," does not exist")
# Define main to make a node object and call inser and print functions
def main():
 my_BST = Node(25)   # creat an object from the node class, I called it my_BST.
 my_BST.insert(19)
 my_BST.insert(28)
 my_BST.insert(13)
 my_BST.insert(9)
 my_BST.insert(30)
 my_BST.insert(17)
 my_BST.insert(26)

 search(my_BST,28,0)
 search(my_BST,17, 0)
 search(my_BST,31,0)
if __name__ == "__main__":
   main()

