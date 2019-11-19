#!python3


# Authors : Lioz elmalem and Ron mor



import networkx as nx
import numpy as np

'''
Assume that difficulty in range(1,5) 
'''


# This function replace 2d array to 1d
def D(mat):
    lm = list()
    for i in range(0 , len(mat)):
        for j in range(0,len(mat[0])):
            lm.append(mat[i][j])
    return lm


# Multiply the values in the matrix
def complete(mat) :
    A = [[0 for x in range(12)] for y in range(12)]

    for i in range(0,12):
        for j in range(0,12):
            if(i < 4) :
                A[i][j] = mat[0][j]
            elif(i > 3 and i < 8) :
                A[i][j] = mat[1][j]
            elif(i > 7):
                A[i][j] = mat[2][j]

    return A


# The main idea of this algorithm is to replace each person with 4 chooses
# because that , i'm multiply the values in the matrix to 12 chooses

def divide_questions(mat) :

    # Every single choice need to get single question
    # and for that , i'm decide to create complete bipartite graph

    G = nx.complete_bipartite_graph(12,12)

    complete(mat)

    _D = D(mat)

    # Update the weights of the edges in graph according to the
    # difficult level to every single node ( student )

    for i, (u, v) in enumerate(G.edges()):
        if(i < len(_D)):
            G.edges[u, v]['weight'] = _D.__getitem__(i)
    
    print("Answer : " , nx.bipartite.minimum_weight_full_matching(G))

    return G

mat = [[5,5,5,5,5,5,5,5,5,5,5,5] ,
       [3,1,3,3,4,5,2,1,5,5,5,5]  ,
       [3,2,2,4,5,3,4,3,1,1,1,1]]

G = divide_questions(mat)


