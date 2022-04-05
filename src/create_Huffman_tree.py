#This file must be import in the main code.
#It creates the Huffman Tree.

from classes.graph_classes import Node
from classes.graph_classes import Binary_tree


def create_all_trees (dictionary) :
    tree_list = []
    for i in dictionary :
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

def create_new_tree (t1, t2, tree_liste) :

    freq = t1.root.frequency + t2.root.frequency
    new_label = t1.root.label + t2.root.label
    newNode = Node(new_label, freq, t1.root, t2.root)
    newTree = Binary_tree(newNode)
    
    new_tree_liste = include_new_tree(newTree, tree_liste)

    return new_tree_liste

def create_Huffman_tree (tree_list) :
    while len(tree_list) > 1 :
        #print(len(tree_list))
        t1 , t2, = tree_list[0], tree_list[1]
        tree_list = create_new_tree(t1, t2, tree_list)
    return tree_list[0]


    