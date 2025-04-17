n = int(input())

for _ in range(n):
    k = int(input())
    
    ans = []
    for i in range(9, 1, -1):
        while k%i == 0:
            k //= i
            ans.append(i)
    
    if k != 1:
        print(-1)
    else:
        ans.sort()
        print(*ans, sep="")