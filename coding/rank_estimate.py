import numpy as np
rank = np.linalg.matrix_rank

from utils import *

def rank_trial(N = 100, m = 200, d = 3, trials = 100):
    print("For reference: (1 - e^{-2d})N = ", (1 - 2.71828**(-2*d)) * N)
    s = 0
    for i in range(trials):
        A = genBGC(N,m,d)
        s += rank(A)
    return s * 1.0/trials
