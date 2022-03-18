# This code create the Huffman Tree

from classes.graph_classes import Node
from classes.graph_classes import Binary_tree


def create_all_trees (dictionary) :
    tree_list = []
    for i in dictionary :
        #print(i)
        N = Node(i, dictionary[i], None, None)
        T = Binary_tree(N)
        tree_list.append(T)
    return tree_list

def include_new_tree (new_tree, list) :
    freq = new_tree.root.frequency
    cand = 0
    for i in enumerate(list) :
        if i[1].root.frequency < freq :
            cand = i[0]
            
    new_list = list[2:cand+1]
    new_list.append(new_tree)
    new_list += list[cand+1:]
    return new_list

'''
def find_minimum_frequencies_trees (tree_list) :
    if tree_list[0].root.frequency <= tree_list[1].root.frequency :
        t1, t2 = tree_list[0], tree_list[1]
    else : t1, t2 = tree_list[1], tree_list[0]

    sum_freq = t1.root.frequency + t2.root.frequency

    for i in range (len(tree_list)) :
        for j in range (i + 1, len(tree_list)) :
            if tree_list[i].root.frequency + tree_list[j].root.frequency < sum_freq :
                if tree_list[i].root.frequency <= tree_list[j].root.frequency :
                    t1, t2 = tree_list[i], tree_list[j]
                else : t1, t2 = tree_list[j], tree_list[i]
    return t1, t2
'''

def create_new_tree (t1, t2, tree_liste) :

    freq = t1.root.frequency + t2.root.frequency
    new_label = t1.root.label + t2.root.label
    newNode = Node(new_label, freq, t1.root, t2.root)
    newTree = Binary_tree(newNode)
    
    new_tree_liste = include_new_tree(newTree, tree_liste)

    for i in tree_liste :
        print(i)
    print("")

    return new_tree_liste

def create_Huffman_tree (tree_list) :
    while len(tree_list) > 1 :
        #print(len(tree_list))
        t1 , t2, = tree_list[0], tree_list[1]
        tree_list = create_new_tree(t1, t2, tree_list)
    return tree_list[0]

'''
if __name__ == "__main__" :
    test = create_all_trees(alphabet_dictionary)    
    
    print(len(test))
    print(test)
    print(" ")
    t1, t2 = find_minimum_frequencies_trees(test)
    new_liste = create_new_tree(t1, t2, test)
    
    for i in new_liste :
        print(i)
    print(len(new_liste))
    print(" ")
    tree = create_Huffman_tree(test)
    print(tree)
    print(tree.root.left_child)
    print(tree.root.right_child.left_child.left_child)
    print(tree.root.right_child.left_child.right_child)
    print(" ")
    print(tree.root.right_child)
    print(tree.root.right_child.left_child)
    '''
    