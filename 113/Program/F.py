import numpy as np

m,n,n,p = map(int, input().split())

A = []
B = []
for i in range(m):
    A.append([x for x in input().split()])
for i in range(n):
    B.append([x for x in input().split()])

A = np.array(A, dtype=int)
B = np.array(B, dtype=int)
C = np.dot(A,B)
for i in C:
    print(*i)