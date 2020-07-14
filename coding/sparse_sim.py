import numpy as np
from utils import genBGC



def count_with_weight(A, weight):
    return (np.sum(A,axis=1) == weight).sum()

def delete_sparse_rows(A, thresh = 3):
    return A[np.sum(A,axis=1) >= thresh, :]

def full_rank(A):
    return np.linalg.matrix_rank(A) == min(A.shape)


# modify this however
def run_sim(N, m, d, trials, thresh=3):
    s = 0
    t = 0
    for i in range(trials):
        A = genBGC(N,m,d)
        if not full_rank(A):
            print("matrix has rank ", np.linalg.matrix_rank(A))
            for j in range(4):
                print("There are ", count_with_weight(A,j), " rows with weight ", j)
    
