#This file implements two classes : Node and Binary_tree which repesnets binary trees.
#This file is imported in the create_Huffman_tree file, in the text_decoding file and in the main file.


class Node :

    """
    This class represents a node in a binary tree.
    """

    def __init__(self, label, frequency, left_child, right_child):
        self.label = label #Label is a string
        self.frequency = frequency #Frequency is an integer
        self.left_child = left_child #Left_child is a Node or None
        self.right_child = right_child #Right_child is a Node or None
        
    def __str__ (self) :
        return self.label

    def is_leaf (self) :

        """
        This method returns 'True' if this node is a leaf in a binary tree.
        """

        if self.left_child == None and self.right_child == None : 
            return True
        return False

    
class Binary_tree :

    """
    This class represent a binary tree.
    A binary tree is define by its root.
    """
    def __init__(self, root):
        self.root = root
    
    def __str__ (self) :
        return self.root.label + ' : ' + str(self.root.frequency)