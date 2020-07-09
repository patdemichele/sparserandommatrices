def compute_P(N, d, R, K): # computes P(r,k) for r<=R k<=K wrt N d
  P = {}
  P[(0,0)] = 1
  for r in range(1,R+1):
    P[(0,r)]=0
  for k in range(1,K+1):
    P[(k,0)] = (1-d/N)^N
    for r in range(1,R+1):
    	P[(r,k)]= P[(r,k-1)] * (1-d*1.0/N)**(N-r) 
    	+ P[(r-1,k-1)] * (1- (1-d*1.0/N)**(N-(r-1)))
  return P