n = int(input())

for _ in range(n):
    # now
    D, M, Y = map(int, input().split("/"))
    # birthday
    d, m, y = map(int, input().split("/"))

    ans = Y-y-1
    if M > m:
        ans += 1
    elif M == m and D >= d:
        ans += 1

    print(ans)