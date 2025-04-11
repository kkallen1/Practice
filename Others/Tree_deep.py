n = int(input())

Tree = {}
for i in range(1, n+1, 1):
    Tree[i] = []

for i in range(n-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)
print(Tree)

Deep = {1:0}
now = 0
def dfs(node, parent):
    global now
    print(f"進入節點 {node}, 父節點為 {parent}")

    if node not in Deep:
        now += 1
    #     Deep[node] = now # 記錄所有節點的深度

    # 只記錄葉子的深度
    if len(Tree[node]) == 1:
        Deep[node] = now
    print(f"now = {now}, {Deep}")


    for child in Tree[node]:
        if child != parent:
            print(f"從節點 {node} 探索子節點 {child}")
            dfs(child, node)
    
    print(f"離開節點 {node}\n")
    now -= 1

dfs(1, -1)
print(Deep)
print(now)
