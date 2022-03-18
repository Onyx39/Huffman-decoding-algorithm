#This is the main code

import get_caracters as gc
import create_Huffman_tree as ht
import text_decoding as td


alphabet_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_freq.txt'
compressed_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_comp.bin'

def create_huffman_tree (alphabet_file_path, compressed_file_path) :
    alphabet_file = open(alphabet_file_path, 'r')
    lines_of_file = alphabet_file.readlines()

    compressed_file = open(compressed_file_path, 'r')

    alphabet_dictionnary = gc.create_alphabet_dictionary(lines_of_file)
    huffman_tree = ht.create_Huffman_tree(ht.create_all_trees(alphabet_dictionnary))

    return(huffman_tree)

tree = create_huffman_tree(alphabet_file_path, compressed_file_path)

binary_code = td.get_binary_code(compressed_file_path)
print(binary_code)

texte_final = td.translate_binary_code(binary_code, tree)
print(texte_final)


