import numpy as np
import scipy.linalg
import networkx as nx
from column_selection import drop_random

# Project1 returns the projection of the 1s vector into 
# the column space of the input matrix
def Project1(matrix):
    rows = np.shape(matrix)[0] #N (number of machines)
    
    #Reduces the matrix to set of linearly independent columns
    matrix = scipy.linalg.orth(matrix)
    #Required as A^T * A is invertible iff the columns are independent 

    matrixTrans = np.transpose(matrix)
    
    #Formula: P = A * (A^T * A)^(-1) * A^T
    projMatrix = np.linalg.inv(np.matmul(matrixTrans, matrix))
    projMatrix = np.matmul(matrix, np.matmul(projMatrix, matrixTrans))
    
    #Multiplies the projMatrix and a vector of all ones with dimension N
    proj = np.matmul(projMatrix, np.ones(rows))
    
    return proj

# Distance1 returns |vector - 1|^2_2
def Distance1(vector):
    difference = vector - np.ones(np.shape(vector)[0])
    dist = np.linalg.norm(difference)
    return np.power(dist,2)

def Error1(matrix):
    return Distance1(Project1(matrix))

# d should divide N
# N/d should divide M, i.e. N should divide M d
def genFRC(N, M, d):
    if N % d != 0 or M % (N/d) != 0:
        print("Warning: uneven groups")
    n_unique_columns = N//d if N%d==0 else N//d + 1
    n_per_group = M//n_unique_columns
    columns = []
    for group in range(n_unique_columns):
        column = np.zeros(N)
        column[group*d : (group+1)*d] = 1
        n_append = n_per_group
        if group == n_unique_columns - 1:
            n_append += M % n_per_group #overflow columns, essentially
        columns += n_append * [column] # add n_append columns
    return np.array(columns).T # transpose it because it will be in row form
        
        
# Creates a random N x m matrix with exactly
# d ones in each column
def genRand(N, m, d):    
    sample_array = np.zeros(N)
    sample_array[:d] = 1
    columns = []    
    for i in range(m):
        np.random.shuffle(sample_array)
        columns += [np.copy(sample_array)]
    return np.array(columns).T

# Creates a random N x m matrix with exactly
# d samples of X ~ [0,1] in each column (all other entries are 0)
def genRandUniform(N, m, d):    
    columns = []    
    for i in range(m):
        sample_array = np.random.rand(N)
        sample_array[d:] = 0
        np.random.shuffle(sample_array)
        columns += [np.copy(sample_array)]
    return np.array(columns).T
    
# Creates a random N x m matrix with
# approximately d ones in each column.
# M_{ij} ~ Binom(1,d/N) for each i,j
def genBGC(N, m, d):
    p = d/N    
    columns = []    
    for i in range(m):
        columns += [np.random.binomial(1, p, N)]
    return np.array(columns).T
    
# Creates a random N x N matrix by sampling
# the set of regular graphs with regularity d and
# returns the adjacency matrix
def genRegular(N, d):
    return nx.to_numpy_matrix(nx.random_regular_graph(d, N))

# generates a d-regular graph on N vertices, drops each column with probability p, reports the error
def test(N,d,p, x, y):
     s = 0
     for i in range(y):
         G = genRegular(N,d)
         for j in range(x):
             s += Error1(drop_random(G, p))
     return s/(x*y)
