"""
This file implements the class 'Node'
This file is imported in the create_Huffman_tree.py file and in the text_decoding.py file
"""

class Node :

    """
    This class represents a node in a binary tree.
    """

    def __init__(self, label : str, frequency : int, left_child, right_child):
        self.label : str = label
        self.frequency  : int= frequency
        self.left_child : Node = left_child
        self.right_child : Node = right_child

    def __str__ (self) -> str :
        return self.label

    def is_leaf (self) -> bool :

        """
        This method returns 'True' if this node is a leaf in a binary tree.
        """

        if self.left_child is None and self.right_child is None :
            return True
        return False
