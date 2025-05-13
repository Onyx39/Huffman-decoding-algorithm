"""
This file decodes the compressed file.
This file is imported to the main file.
"""

import get_caracters as gc
import paths as p


def get_binary_code (compressed_file_path : str) -> str :

    """
    Input : The path to the compressed file as a string
    Output : A string
    This function returns the binary code of the compressed file.
    """

    binary = ""
    with open(compressed_file_path, 'rb') as f:
        contents = f.read()
        for i in contents :
            cand = bin(i)[2:]
            while len(cand) < 8 :
                cand = '0' + cand
            binary += cand
    return binary


def translate_binary_code(binary_code, huffman_tree) :

    """
    Inputs : The binary code of the compressed file as a string
             and the Huffman tree as a binary tree
    Output : A string
    This function returns the decoded text as a string.
    """

    result = ""
    with open(p.ALPHABET_FILE_PATH, 'r', encoding="utf-8") as alphabet_file :
        # alphabet_file = open(p.alphabet_file_path, 'r')
        lines_of_file = alphabet_file.readlines()
        lenght = gc.create_alphabet_dictionary(lines_of_file)[1]
        current_node = huffman_tree.root
        for i in binary_code :
            if not current_node.is_leaf() :
                if i == '0' :
                    current_node = current_node.left_child
                else :
                    current_node = current_node.right_child
            else :
                result += current_node.label
                current_node = huffman_tree.root
                if i == '0' :
                    current_node = current_node.left_child
                else :
                    current_node = current_node.right_child
                if len(result) == lenght :
                    return result
    return result
