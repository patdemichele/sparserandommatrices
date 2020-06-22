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
