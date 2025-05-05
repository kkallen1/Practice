# APCS 2016 3月 第3題 線段覆蓋長度

n = int(input())
List = [ tuple(map(int, input().split())) for _ in range(n)]
List = sorted(List)

ans = 0
start, end = List[0]
for a, b in List[1::]:
    if a <= end:
        end = max(end, b)
    else:
        ans += end - start
        start, end = a, b
        
ans += end - start
    
print(ans)
