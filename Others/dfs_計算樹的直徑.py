n = int(input())

Tree = {}
for i in range(1, n+1, 1):
    Tree[i] = []

for i in range(n-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)
print(Tree)


max_diameter = 0
def dfs(node, parent):
    global max_diameter
    print(f"進入節點 {node}, 父節點為 {parent}")

    # 記錄當前節點到其子樹中葉節點的最大深度和次大深度
    max_depth = 0
    second_max_depth = 0


    for child in Tree[node]:
        if child != parent:
            print(f"從節點 {node} 探索子節點 {child}")
            depth = dfs(child, node)

            # 更新最大深度和次大深度
            if depth > max_depth:
                max_depth, second_max_depth = depth, max_depth
            elif depth > second_max_depth:
                second_max_depth = depth
            
            print(f"子節點{child}的深度 {depth}, 目前最大深度 {max_depth}, 次大深度 {second_max_depth}\n")
    
    # 更新全局最大直徑（考慮經過當前節點的路徑）
    max_diameter = max(max_diameter, max_depth + second_max_depth)

    print(f"離開節點 {node}")
    return max_depth +1

dfs(1, -1)
print(max_diameter)
