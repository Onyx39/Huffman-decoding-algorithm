"""
This code gets the alphabet of the file and the frequencies of the caracters
This file is imported in the text_decoding file and in the main file.
"""

def extract_frequency (line) :

    """
    Input : A line of the alphabet file
    Output : An integer
    This file returns the frequency that appaers in the line given as a parameter.
    """

    end = len(line)
    frequency = line[2:end]
    return int(frequency)


def create_alphabet_dictionary (file_lines) :

    """
    Input : The list of strings of the alphabet file
    Outputs : A dictionnary and an integer
    This function returns a dictionnary that contains all the caracters of the decoded file
        and their frecencies in the text.
    Moreover, it returns the lenght of the decoded text.
    """

    dictionary = {}
    lenght = 0
    for i in range (1, len(file_lines)) :
        lenght += extract_frequency(file_lines[i])
        dictionary[str(file_lines[i][0])] = extract_frequency(file_lines[i])
    return dictionary, lenght
