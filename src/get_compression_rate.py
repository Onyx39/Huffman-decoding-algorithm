#This file must be import in the main code.
#It gets the compression rate of the compressed file.

def get_file_size (path) :
    file = open(path, 'r')
    file_size = 0
    while True :
        element = file.read(1)
        if not element :
            break
        else :
            file_size += 1
    return file_size

def get_compression_rate (compressed_file_path, normal_file_path) :
    compressed_file_size = get_file_size(compressed_file_path)
    normal_file_size = get_file_size(normal_file_path)
    result = compressed_file_size/normal_file_size
    return result


                   