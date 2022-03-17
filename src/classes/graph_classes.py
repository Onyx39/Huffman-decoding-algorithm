#This code has to be imported in the main code
#It creates the Haufman tree with the alphabet


class Node :
    """Classe qui représente les noeuds d'un arbre binaire"""
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
    
class Binary_tree :
    """Classe qui représente un arbre binaire"""
    def __init__(self, root):
        self.root = root
    
    def __str__ (self) :
        return self.root.label + ' : ' + str(self.root.frequency)