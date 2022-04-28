#This file decodes the compressed file.
#This file is imported to the main file.


from classes.Node import Node
import get_caracters as gc
import paths as p


def get_binary_code (compressed_file_path) :

    """
    Input : The path to the compressed file as a string
    Output : A string
    This function returns the binary code of the compressed file.
    """

    str = ""
    with open(compressed_file_path, 'rb') as f:
        contents = f.read()
        for i in contents :
            cand = (bin(i)[2:])
            while len(cand) < 8 :
                cand = '0' + cand
            str += cand    
    return str


def translate_binary_code(binary_code, huffman_tree) :

    """
    Inputs : The binary code of the compressed file as a string and the Huffman tree as a binary tree
    Output : A string
    This function returns the decoded text as a string.
    """

    text = ""
    alphabet_file = open(p.alphabet_file_path, 'r')
    lines_of_file = alphabet_file.readlines()
    lenght = gc.create_alphabet_dictionary(lines_of_file)[1]
    current_node = huffman_tree.root
    for i in binary_code : 
        if current_node.is_leaf() == False :
            if i == '0' :
                current_node = current_node.left_child
            else : 
                current_node = current_node.right_child
        else :
            text += current_node.label
            current_node = huffman_tree.root
            if i == '0' :
                current_node = current_node.left_child
            else : 
                current_node = current_node.right_child
            if len(text) == lenght :
                return text
    return text