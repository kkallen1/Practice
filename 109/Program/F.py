n = int(input())

for _ in range(n):
    a = [int(x) for x in input().split()]

    ans = -65535

    for i in range( len(a) ):
        kk = 0
        for j in range(i, len(a) ):
            kk += a[j]
            if kk > ans:
                ans = kk
    
    print(ans)