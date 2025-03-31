m = int(input()) # 選擇要輸出第幾名的能力值
n = int(input()) # 有幾個角色
L = []           # 輸入的資料
L1 = []          # 計算後的能力值
for _ in range(n):
    a, b = map(int, input().split())
    L.append([a,b])
    L1.append(a**2 + b**2)

# 氣泡排序法
for i in range(n):
    for j in range(n-i-1):
        if L1[j] > L1[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            L1[j], L1[j+1] = L1[j+1], L1[j]

print(*L[m-1])
