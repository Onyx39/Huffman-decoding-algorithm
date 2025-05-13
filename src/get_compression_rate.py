"""
This file gets the compression rate of the compressed file.
This file is imported in the main file.
"""

def get_file_size (path) :

    """
    Input : A path to a file as a string
    Output : An integer
    This function returns the size of a file.
    """

    with open(path, 'rb') as file:
        # file = open(path, 'r')
        file_size = 0
        while True :
            element = file.read(1)
            if not element :
                break
            file_size += 1
    return file_size


def get_compression_rate (compressed_file_path, normal_file_path) :

    """
    Inputs : The file to the compressed file and the path to the decoded text as strings
    Output : A float
    This file returns the compression rate of the compressed file.
    """

    compressed_file_size = get_file_size(compressed_file_path)
    normal_file_size = get_file_size(normal_file_path)
    result = compressed_file_size/normal_file_size
    return result
