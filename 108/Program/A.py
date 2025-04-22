n = int(input())

for _ in range(n):
    a = input()

    ans, tmp = 0, 0
    kk = 1
    for i in a:
        if i == "O":
            ans += kk
            kk += 1
        else:
            kk = 1

    print(ans)