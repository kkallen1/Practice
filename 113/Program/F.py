m, n, n, p = map(int, input().split())

List1 = []
List2 = []
for i in range(m):
    L = [int(x) for x in input().split()]
    List1.append(L)
for i in range(n):
    L = [int(x) for x in input().split()]
    List2.append(L)

ans = [[0]*p for _ in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            ans[i][j] += List1[i][k]*List2[k][j]

for i in ans:
    print(*i)

# 使用庫
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
