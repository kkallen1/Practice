# 01
List = []
r, c = map(int, input().split())
for i in range(r):
    List.append( [x for x in input().split()] )

for i in range(c):
    for kk in List:
        print(kk[i], end=" ")
    print()

# 02
m, n = map(int, input().split())
List = [[0]*m for _ in range(n)]
for i in range(m):
    L = [int(x) for x in input().split()]

    for j in range(n):
        List[j][i] = L[j]

for i in List:
    print(*i)

# 使用庫
import numpy as np

m,n = map(int, input().split())

A = []
for i in range(m):
    A.append([x for x in input().split()])

A = np.array(A, dtype=int)
C = A.T
for i in C:
    print(*i)
