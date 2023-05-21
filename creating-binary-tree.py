# ************* Creating binary tree using both recursive method *************


# Create a class that will be the root node (or parent node)
class Node:
    # Initialize a constructor with parameter -data
    def __init__(self, data):
        # If we create object of Node class named root then
        # root.left = None
        # root.right = None
        # root.data = data

        self.left = None
        self.right = None
        self.data = data

    # Define an insert method that functions to create node if not present or add value to an empty node
    def insert(self, value):
        # Check if main Node is empty, if so then the first value inserted will be the root node (or parent node)
        if self.data:
            # Check the inserted value to parent node value
            if value < self.data:
                if self.left is None:
                    self.left = Node(
                        value
                    )  # Creating a node for root.left with inserted value
                else:
                    # If root.left node is present then use recursive call to insert function to insert value to that node
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value

    # Define print function to print the tree of inserted values
    def printTree(self):
        print(self.data)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()


# Object of class Node created with the name called root and calling the insert method with some value
root = Node(12)
root.insert(8)
root.insert(4)
root.insert(14)
root.insert(20)
root.printTree()
