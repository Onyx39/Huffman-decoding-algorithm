"""
This is the main code you have to run.
Don't forget to modify all the paths in the paths.py file!
"""

import get_caracters as gc
import create_huffman_tree as ht
import text_decoding as td
import get_compression_rate as cr
import paths as p


def get_the_tree () : #alphabet_file_path) :

    """
    Input : The path to the alphabet file
    Output : A binary tree
    This function creates the Huffman tree with the paths given in the paths.py file.
    """

    with open(p.ALPHABET_FILE_PATH, 'r', encoding='utf-8') as alphabet_file :
        lines_of_file = alphabet_file.readlines()
        alphabet_dictionnary = gc.create_alphabet_dictionary(lines_of_file)[0]
        huffman_tree = ht.create_huffman_tree(ht.create_all_trees(alphabet_dictionnary))
        return huffman_tree


def get_final_text () : #alphabet_file_path, compressed_file_path) :

    """
    Inputs : The paths to the alphabet file and to the compressed file
    Outputs : A binary tree and two strings
    This function returns the binary code of the compressed file and the decoded text as strings.
    It also returns the huffman tree.
    """

    tree = get_the_tree() #p.ALPHABET_FILE_PATH)
    binary_code = td.get_binary_code(p.COMPRESSED_FILE_DATA)
    texte_final = td.translate_binary_code(binary_code, tree)
    return tree, binary_code, texte_final


def get_efficiency () : #alphabet_file_path, compressed_file_path, path) :

    """
    Inputs : The paths to the alphabet file and to the compressed file
    Output : A float
    This function returns the compresion rate of the compressed file.
    This function prints some information about the compression rate in the console.
    """

    # tree, binary_code, final_text = get_final_text(p.ALPHABET_FILE_PATH, p.COMPRESSED_FILE_DATA)
    # message = td.translate_binary_code(binary_code, tree)
    compression_rate = cr.get_compression_rate(p.COMPRESSED_FILE_DATA, p.DECOMPRESSED_FILE_PATH)
    print("The compressed file contains " + str(round(1/compression_rate, 2)) + " caracters/byte.")
    print("The compression rate is " + str(round(compression_rate*100, 2)), '%.')
    return compression_rate


def get_decompressed_file (path) : #alphabet_file_path, compressed_file_path, path) :

    """
    Inputs : The paths to the alphabet file, to the compressed file and to the empty file
    Output : Nothing
    This function creates a file that contains the decoded data.
    """

    tree, binary_code, _ = get_final_text() #p.ALPHABET_FILE_PATH, p.COMPRESSED_FILE_DATA)
    message = td.translate_binary_code(binary_code, tree)
    with open(path, "w", encoding='utf-8') as new_file :
        new_file.write(message)
        new_file.close()


def run_the_whole_program () :

    """
    Input : Nothing
    Output : Nothing
    Runs the whole programm : it saves the decoded data and prints the compression rate.
    """

    get_decompressed_file(p.DECOMPRESSED_FILE_PATH)
    #p.ALPHABET_FILE_PATH, p.COMPRESSED_FILE_DATA, p.DECOMPRESSED_FILE_PATH)
    print(" ")
    get_efficiency() #p.ALPHABET_FILE_PATH, p.COMPRESSED_FILE_DATA, p.DECOMPRESSED_FILE_PATH)
    print(" ")

run_the_whole_program()
