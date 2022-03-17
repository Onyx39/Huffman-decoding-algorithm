#This file must be import in the main code
#It gets the alphabet of the file and the frequancies of the caracters


def get_alphabet_size(file_lines) :
    return int(file_lines[0][0])

def extract_frequency (line) :
    end = len(line) - 1
    frequency = line[2:end]
    return int(frequency)

def create_alphabet_dictionary (file_lines) :
    dictionary = {}
    for i in range (1, len(file_lines)) :
        dictionary[str(file_lines[i][0])] = extract_frequency(file_lines[i])
    return dictionary


if __name__ == '__main__' :

    alphabet_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_freq.txt'
    compressed_file_path = 'C:/Users/val_p/Desktop/PROJ631/1_Python_Decompression_Huffman/exemple_comp.bin'

    alphabet_file = open(alphabet_file_path, 'r')
    lines_of_file = alphabet_file.readlines()

    compressed_file = open(compressed_file_path, 'r')
    
    '''
    print(lines_of_file)
    print(lines_of_file[0])
    print(lines_of_file[1])
    print(lines_of_file[2])
    
    print (get_alphabet_size(lines_of_file))
    print(create_alphabet_dictionary(lines_of_file))
    '''