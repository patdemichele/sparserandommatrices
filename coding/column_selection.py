import numpy as np
import scipy.linalg



# params: A: np array with shape (N,M), p a probability that each column is dropped
def drop_random(A, p):
    (N,M) = A.shape
    cols = (np.random.rand(M) > p).astype(int)
    selection_mat = np.identity(M) * np.outer(cols, cols)
    return A.dot(selection_mat)
    # M by M matrix to select columns


