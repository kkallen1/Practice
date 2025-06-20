"""
疑似 CPE 2025/5/20 題目

zj c074
1. 使用 itertools 的 combinations。(指定長度的組合，類似 C a取b)
2. 排列組合的長度固定為 6
3. ans 儲存所有測資的所有排列組合
4. 輸出

備註:
輸出格式要注意，測資與測資之間會有空行 => 除了最後一組測資外，其餘皆要空行再輸出下一組解
"""

from itertools import combinations

ans = []
while True:
    a = list(map(int, input().split()))
    if a[0]:
        a.pop(0)
        b = 6
        
        ans.append(sorted(combinations(a, b)))
    else:
        break

# 每組的答案之前要有空行，最後一組不能有空行
for i in ans[:-1:]:
    for j in i:
        print(*j, sep=" ")
    print()
for i in ans[-1]:
    print(*i, sep=" ")
