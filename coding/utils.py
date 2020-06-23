import numpy as np
import scipy.linalg


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


