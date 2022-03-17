#This is the main code

import get_caracters as gc
import create_Huffman_tree as ht


alphabet_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_freq.txt'
compressed_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_comp.bin'

alphabet_file = open(alphabet_file_path, 'r')
lines_of_file = alphabet_file.readlines()

compressed_file = open(compressed_file_path, 'r')

alphabet_dictionnary = gc.create_alphabet_dictionary(lines_of_file)
huffman_tree = ht.create_Huffman_tree(ht.create_all_trees(alphabet_dictionnary))

print(huffman_tree)


