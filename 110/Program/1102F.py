n = int(input())
L = [int(x) for x in input().split()]

ans = 0
for i in range(1, n, 1):
    for j in range(0, i, 1):
        if L[j] > L[i]:
            ans += 1

print(ans)
