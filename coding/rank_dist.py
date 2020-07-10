def compute_Q(N, d, R, K): # computes Q(r,k) \leq P(r,k) for r<=R k<=K wrt N d
  Q = {}
  Q[(0,0)] = 1
  for r in range(1,R+1):
    Q[(r,0)]=0
  for k in range(1,K+1):
    Q[(0,k)] = (1-d*1.0/N)**(N * k)
    for r in range(1,R+1):
      Q[(r,k)]= Q[(r,k-1)] * (1-d*1.0/N)**(N) + Q[(r-1,k-1)] * (1- (1-d*1.0/N)**(N-(r-1)))
  return Q
