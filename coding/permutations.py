import numpy as np
import scipy
def row_col_equal(A):
    r1 = np.sum(A[0,:])
    return (np.sum(A, axis=0) == r1).all() and (np.sum(A, axis=1) == r1).all()
