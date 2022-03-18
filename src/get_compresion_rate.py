#comment

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

def get_compresion_rate (compressed_file_path, normal_file_path) :
    compressed_file_size = get_file_size(compressed_file_path)
    normal_file_size = get_file_size(normal_file_path)
    result = 1 - (compressed_file_size/normal_file_size)
    return result


                   