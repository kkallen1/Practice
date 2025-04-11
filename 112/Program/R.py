# https://github.com/kkallen1/Practice/blob/main/Others/dfs_%E8%A8%88%E7%AE%97%E6%A8%B9%E7%9A%84%E7%9B%B4%E5%BE%91.py
# https://github.com/kkallen1/Practice/blob/main/Others/dfs_計算樹的直徑.py

n = int(input())

Tree = {}
for i in range(1, n+1, 1):
    Tree[i] = []

for i in range(n-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

max_diameter = 0
def dfs(node, parent):
    global max_diameter

    # 記錄當前節點到其子樹中葉節點的最大深度和次大深度
    max_depth = 0
    second_max_depth = 0


    for child in Tree[node]:
        if child != parent:
            depth = dfs(child, node)

            # 更新最大深度和次大深度
            if depth > max_depth:
                max_depth, second_max_depth = depth, max_depth
            elif depth > second_max_depth:
                second_max_depth = depth
    
    # 更新全局最大直徑（考慮經過當前節點的路徑）
    max_diameter = max(max_diameter, max_depth + second_max_depth)

    return max_depth +1

dfs(1, -1)
print(max_diameter)
