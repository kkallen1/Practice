import numpy as np

m,n = map(int, input().split())

A = []
for i in range(m):
    A.append([x for x in input().split()])

A = np.array(A, dtype=int)
C = A.T
for i in C:
    print(*i)