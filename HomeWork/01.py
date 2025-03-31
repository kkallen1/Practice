"""m391 改
https://zerojudge.tw/ShowProblem?problemid=m931
"""

m = int(input()) # 選擇要輸出第幾名的能力值
n = int(input()) # 有幾個角色
L = []           # 輸入的資料
L1 = []          # 計算後的能力值
for _ in range(n):
    a, b = map(int, input().split())
    L.append([a,b])
    L1.append(a**2 + b**2)

for i in range(m):
    if i == m-1:
        print(*L[L1.index(max(L1))])
        break
    L.remove(L[L1.index(max(L1))])
    L1.remove(L1[L1.index(max(L1))])
