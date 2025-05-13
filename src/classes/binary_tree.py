"""
This file implements the class 'Binary_tree'.
This file is imported in the create_Huffman_tree.py file
"""

class BinaryTree :

    """
    This class represent a binary tree.
    A binary tree is define by its root.
    """
    def __init__(self, root):
        self.root = root

    def __str__ (self) :
        return self.root.label + ' : ' + str(self.root.frequency)
