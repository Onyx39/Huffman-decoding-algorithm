"""
This file creates the Huffman tree which enables to decode the compressed file.
This file is imported in the main file.
"""

from classes.node import Node
from classes.binary_tree import BinaryTree


def create_all_trees (dictionary) :

    """
    Input  : A dictionnary that contains all the caracters in the decoded text and their frequencies
    Output : A list of binary trees
    This function creates as many binary trees as the number of caracters in the decoded file.
    This list is ordered by the frequencies of the roots in the ascending order.
    """

    tree_list = []
    for i in dictionary :
        root = Node(i, dictionary[i], None, None)
        tree = BinaryTree(root)
        tree_list.append(tree)
    return tree_list


def include_new_tree (new_tree, tree_list) :

    """
    Inputs : A binary tree and a list of biary trees
    Output : A list of binary tree
    This function add a binary tree in a list of binary tree
        without changing the ascending order of the frequencies.
    """

    freq = new_tree.root.frequency
    cand = 0
    for i in enumerate(tree_list) :
        if i[1].root.frequency < freq :
            cand = i[0]
    new_list = tree_list[2:cand+1]
    new_list.append(new_tree)
    new_list += tree_list[cand+1:]
    return new_list


def create_new_tree (t1, t2, tree_liste) :

    """
    Inputs : Two binary trees and a list of binary trees
    Output : A list of binary trees
    This function creates a new binary tree with the the two trees given as parameters
        and include it in the list of binary trees without changing the ascending order.
    """

    freq = t1.root.frequency + t2.root.frequency
    new_label = t1.root.label + t2.root.label
    new_node = Node(new_label, freq, t1.root, t2.root)
    new_tree = BinaryTree(new_node)
    new_tree_liste = include_new_tree(new_tree, tree_liste)
    return new_tree_liste


def create_huffman_tree (tree_list) :

    """
    Input : A list of binary trees where each binary tree represents a caracter of the text
    Output  : A binary tree
    This function returns the Huffman tree and need the result of the create_all_trees function.
    """

    while len(tree_list) > 1 :
        t1 , t2, = tree_list[0], tree_list[1]
        tree_list = create_new_tree(t1, t2, tree_list)
    return tree_list[0]
