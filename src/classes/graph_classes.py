#This code implements two classes : Node and Binary_tree which repesnets binary trees.
#This code is imported in the create_Huffman_tree file, in the text_decoding file and in the main file.


class Node :

    """
    This class represents a node in a binary tree.
    """

    def __init__(self, label, frequency, left_child, right_child):
        self.label = label
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child 
        
    def __str__ (self) :
        return self.label
    
    def add_left_child (self, label):
        self.fils_g = Node(label, None, None)
        return self
    
    def add_right_child (self, label):
        self.fils_d = Node(label, None, None)
        return self

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