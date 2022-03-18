#This is the main code

import get_caracters as gc
import create_Huffman_tree as ht
import text_decoding as td
import get_compresion_rate as cr


alphabet_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_freq.txt'
compressed_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_comp.bin'

def create_huffman_tree (alphabet_file_path, compressed_file_path) :
    alphabet_file = open(alphabet_file_path, 'r')
    lines_of_file = alphabet_file.readlines()

    alphabet_dictionnary = gc.create_alphabet_dictionary(lines_of_file)
    huffman_tree = ht.create_Huffman_tree(ht.create_all_trees(alphabet_dictionnary))

    return(huffman_tree)

tree = create_huffman_tree(alphabet_file_path, compressed_file_path)

binary_code = td.get_binary_code(compressed_file_path)
print(binary_code)

texte_final = td.translate_binary_code(binary_code, tree)
print(texte_final)

print(cr.get_file_size(compressed_file_path))

#print(cr.get_compresion_rate(compressed_file_path, ))

def get_truc_average (message, path) :
    size = cr.get_file_size(compressed_file_path)
    nb_caracters = len(message) - 2
    print("The compressed file contains " + str(nb_caracters/size) + " caracters per bytes")
    print("The compression rate is " + str(size/nb_caracters))
    return size/nb_caracters

get_truc_average(texte_final, compressed_file_path)