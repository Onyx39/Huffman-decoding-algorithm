#This is the main code you have to run.
#Don't forget to create an empty text file on your machine and to update all the paths in the paths.py file!


import get_caracters as gc
import create_Huffman_tree as ht
import text_decoding as td
import get_compression_rate as cr
import paths as p


def create_huffman_tree (alphabet_file_path, compressed_file_path) :

    """
    Inputs : The paths to the alphabet file and to the compressed file
    Output : A binary tree
    This function creates the Huffman tree with the paths given in the paths.py file.
    """
    
    alphabet_file = open(p.alphabet_file_path, 'r')
    lines_of_file = alphabet_file.readlines()
    alphabet_dictionnary = gc.create_alphabet_dictionary(lines_of_file)[0]
    huffman_tree = ht.create_Huffman_tree(ht.create_all_trees(alphabet_dictionnary))
    return huffman_tree


def get_final_text (alphabet_file_path, compressed_file_path) :

    """
    Inputs : The paths to the alphabet file and to the compressed file
    Outputs : A binary tree and two strings
    This function returns the binary code of the compressed file and the decoded text as strings.
    It also returns the huffman tree.
    """
    
    tree = create_huffman_tree(p.alphabet_file_path, p.compressed_file_path)
    binary_code = td.get_binary_code(p.compressed_file_path)
    texte_final = td.translate_binary_code(binary_code, tree)
    return tree, binary_code, texte_final


def get_efficiency (alphabet_file_path, compressed_file_path, path) :

    """
    Inputs : The paths to the alphabet file and to the compressed file
    Output : A float
    This function returns the compresion rate of the compressed file.
    This function prints some information about the compression rate in the console.
    The file that contains the final code must be filled by programm.
    """
    
    tree, binary_code, texte_final = get_final_text(p.alphabet_file_path, p.compressed_file_path)
    message = td.translate_binary_code(binary_code, tree)
    compression_rate = cr.get_compression_rate(p.compressed_file_path, p.decompressed_file_path)
    print("The compressed file contains " + str(round(1/compression_rate, 2)) + " caracters/bytes.")
    print("The compression rate is " + str(round(compression_rate*100, 2)), '%.')
    return compression_rate


def get_decompressed_file (alphabet_file_path, compressed_file_path, path) :

    """
    Inputs : The paths to the alphabet file, to the compressed file and to the empty file
    Output : Nothing
    This file write the decoded text in the empty file.
    """
    
    tree, binary_code, texte_final = get_final_text(p.alphabet_file_path, p.compressed_file_path)
    message = td.translate_binary_code(binary_code, tree)
    new_file = open(path, "w")
    new_file.write(message)
    new_file.close()


def run_the_whole_programm () :
    
    """
    Input : Nothing
    Output : Nothing
    This function run thhe whole programm : 
    it writes the decoded message in the empty file and prints the compression rate.
    
    """
    
    get_decompressed_file(p.alphabet_file_path, p.compressed_file_path, p.decompressed_file_path)
    print(" ")
    get_efficiency(p.alphabet_file_path, p.compressed_file_path, p.decompressed_file_path)
    print(" ")

run_the_whole_programm()

