n = int(input())

Tree = [[0]*(n+1) for _ in range(n+1)]

# 填入索引
for i in range(n+1):
    Tree[0][i] = i  # 第一行
    Tree[i][0] = i  # 第一列

edges = []
for i in range(n-1):
    a, b = map(int, input().split())
    edges.append((a,b))

for u,v in edges:
    Tree[u][v] = 1
    # Tree[v][u] = 1 # 反向

for row in Tree:
    print(row)