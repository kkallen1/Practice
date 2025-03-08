"""m391 改
https://zerojudge.tw/ShowProblem?problemid=m931
"""

m = int(input()) # 選擇要輸出第幾名的能力值
n = int(input()) # 有幾個角色
L = []
L1 = []
for _ in range(n):
    a, b = map(int, input().split())
    L.append([a,b])
    L1.append(a**2 + b**2)

print(*L[L1.index(max(L1))])
