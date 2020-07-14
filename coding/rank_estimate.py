import numpy as np
rank = np.linalg.matrix_rank

from utils import *

def rank_trial(N = 100, m = 200, d = 3, trials = 100):
    print("For reference: (1 -d/N}^{2N}*N = ", (1-(1 - d*1.0/N)**(2*N)) * N)
    s = 0
    for i in range(trials):
        A = genBGC(N,m,d)
        s += rank(A)
    return s * 1.0/trials
