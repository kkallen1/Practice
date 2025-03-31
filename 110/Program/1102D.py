n = int(input())
L = [int(x) for x in input().split()]

ans = sum(L)
if ans%2 != 0:
    L.sort()
    kk = 1
    for i in L:
        if i%2 != 0:
            kk = i
            break

    ans = sum(L)-kk
print(ans)
