# c463. apcs 樹狀圖分析 (Tree Analyses)
# 找root及所有節點的高度總和.py
# TLE code
n = int(input())

Tree = {}
for i in range(1, n+1, 1):
    Tree[i] = []

for i in range(1, n+1, 1):
    k = list(input().split())
    for node in k[1::]:
        Tree[i].append(int(node))

# print(Tree)
List = [int(x) for x in range(1, n+1, 1)]
for i in range(1, n+1, 1):
    for node in Tree[i]:
        if node in List:
            List.remove(node)

root = List[0]

ans = 0
def f(node):
    global ans

    if len(Tree[node]) == 0:
        return 0
    
    hights = []
    for i in Tree[node]:
        hights.append(f(i))

    node_height = 1 + max(hights)
    
    ans += node_height
    return node_height

f(root)
print(root)
print(ans
