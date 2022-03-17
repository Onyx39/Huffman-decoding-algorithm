#This is the main code

import get_caracters as gc

alphabet_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_freq.txt'
compressed_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_comp.bin'

alphabet_file = open(alphabet_file_path, 'r')
lines_of_file = alphabet_file.readlines()

compressed_file = open(compressed_file_path, 'r')
    

print(lines_of_file)
print(lines_of_file[0])
print(lines_of_file[1])
print(lines_of_file[2])
    
print(gc.get_alphabet_size(lines_of_file))
print(gc.create_alphabet_dictionary(lines_of_file))
