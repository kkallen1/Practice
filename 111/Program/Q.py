n = int(input())

Tree = {}
for i in range(n):
    Tree[i] = []

for i in range(n):
    a, b, c = map(int, input().split())

    if b != -1:
        Tree[a].append(b)
    if c != -1:
        Tree[a].append(c)
# print(Tree)

def f(node):
    if not Tree[node]:
        return 1
    return max(f(child) for child in Tree[node])+1
    
ans = {}
    
Deep = {}
now = -1
def dfs(node, parent):
    global now
    # print(f"進入節點 {node}, 父節點為 {parent}")

    if node not in Deep:
        now += 1
        Deep[node] = now # 記錄所有節點的深度

    # 只記錄葉子的深度
    # if len(Tree[node]) == 1:
    #     Deep[node] = now
    # print(f"now = {now}, {Deep}")

    height = f(node)-1
    # print(f"node = {node}, height = {height-1}")

    ans[node] = [node, parent, len(Tree[node]), now, height]

    for child in Tree[node]:
        if child != parent:
            # print(f"從節點 {node} 探索子節點 {child}")
            dfs(child, node)
    
    # print(f"離開節點 {node}\n")
    now -= 1

dfs(0, -1)
ans = dict(sorted(ans.items()))
# print(ans)

for key, item in ans.items():
    print(f"node {item[0]}: parent = {item[1]}, degree = {item[2]}, depth = {item[3]}, height = {item[4]},")
# print(Deep)
