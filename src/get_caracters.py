#This file must be import in the main code
#It gets the alphabet of the file and the frequancies of the caracters

def get_alphabet_size(file_lines) :
    return int(file_lines[0][0])

def extract_frequency (line) :
    end = len(line)
    frequency = line[2:end]
    return int(frequency)

def create_alphabet_dictionary (file_lines) :
    dictionary = {}
    lenght = 0
    for i in range (1, len(file_lines)) :
        lenght += extract_frequency(file_lines[i])
        dictionary[str(file_lines[i][0])] = extract_frequency(file_lines[i])
    return dictionary, lenght

