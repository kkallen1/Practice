"""
APCS 2023 10月 第2題 交錯字串
zj m371

dada878: https://dada878.com/blogs/apcs-2023-10-solution
"""

# NA code
n, m = map(int, input().split())

List = [[int(x) for x in input().split()] for _ in range(n)]

ans = 0
for _ in range(n*m):
    for i in range(n):
        for j in range(m):
            if List[i][j] == -1:
                continue
            
            if i>0:
                k = i-1
                while k>=0 and List[k][j] == -1:
                    k -= 1
                if List[i][j] == List[k][j]:
                    ans += List[i][j]
                    List[i][j] = List[k][j] = -1
                    continue
            
            if j>0:
                k = j-1
                while k>=0 and List[i][k] == -1:
                    k -= 1
                if List[i][j] == List[i][k]:
                    ans += List[i][j]
                    List[i][j] = List[i][k] = -1
                    continue
                
print(ans)
