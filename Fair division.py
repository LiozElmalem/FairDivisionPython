#!python3

import networkx as nx

'''
Assume that difficulty in range(1,5) 
'''


def divide_questions(mat) :
    num_students  = len(mat)
    num_questions = len(mat[0])

    G = nx.Graph()

    for i in range(0 , num_questions) :
        for j in range(0 , num_questions) :
            if(i < 4) :
                G.add_edge(i , j , weight = mat[0][j])
            elif(i < 8 and i > 3) :
                G.add_edge(i, j, weight = mat[1][j])
            elif(i < 12 and i > 7) :
                G.add_edge(i, j, weight = mat[2][j])

    print("Answer : " , nx.max_weight_matching(G))


mat = [[5,5,5,5,5,5,5,5,5,5,5,5] ,
       [3,1,3,3,4,5,2,1,5,5,5,5]  ,
       [3,2,2,4,5,3,4,3,1,1,1,1]]
divide_questions(mat)

