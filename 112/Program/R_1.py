class Tree():
    def __init__(self, data=None):
        self.data = data
        self.line = set()
    
    def i(self, other_node):
        self.line.add(other_node)
        other_node.line.add(self)

n = int(input())

tree = {}
for i in range(1, n+1):
    tree[i] = Tree(i)

for _ in range(n-1):
    a, b = map(int, input().split())

    tree[a].i(tree[b])
    tree[b].i(tree[a])

def f(node, parent):
    kk = []
    for now in tree[node].line:
        if now.data != parent:
            depth, deep_node = f(now.data, node)
            kk.append((depth+1, deep_node))
    
    if kk:
        depth, deep_node = max(kk, key=lambda x: x[0])
        return depth, deep_node
    return 0, node

_, node = f(5, -1)
depth, _ = f(node, -1)
print(depth)
