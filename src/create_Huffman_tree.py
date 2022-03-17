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

def create_new_tree (t1, t2, tree_liste) :
    freq = t1.root.frequency + t2.root.frequency
    newNode = Node('new Tree', freq, t1, t2)
    newTree = Binary_tree(newNode)
    
    tree_liste.remove(t1)
    tree_liste.remove(t2)
    tree_liste.append(newTree)

    return tree_liste

def create_Huffman_tree (tree_list) :
    while len(tree_list) > 1 :
        #print(len(tree_list))
        t1 , t2, = find_minimum_frequencies_trees(tree_list)
        tree_list = create_new_tree(t1, t2, tree_list)
    return tree_list[0]


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
    print(tree.root.right_child.root.left_child.root.left_child)
    print(tree.root.right_child.root.left_child.root.right_child)
    print(" ")
    print(tree.root.right_child)
    print(tree.root.right_child.root.left_child)
    