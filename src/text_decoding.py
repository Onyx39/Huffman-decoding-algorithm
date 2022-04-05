#This file must be import in the main code.
#It decods the compressed file.


from classes.graph_classes import Node

def get_binary_code (compressed_file_path) :
    str=""
    with open(compressed_file_path, 'rb') as f:
        contents = f.read()
    for i in contents :
        cand = (bin(i)[2:])
        while len(cand) < 8 :
            cand = '0' + cand
        str += cand
    return str


def translate_binary_code(binary_code, huffman_tree) :
    text =""
    current_node = huffman_tree.root
    for i in binary_code :
        #print(i)
        #print(type(i))
        if current_node.is_leaf() == False :
            if i == '0' :
                current_node = current_node.left_child
            else : current_node = current_node.right_child
        else : 
            text += current_node.label
            current_node = huffman_tree.root
            if i == '0' :
                current_node = current_node.left_child
            else : current_node = current_node.right_child
    return text
