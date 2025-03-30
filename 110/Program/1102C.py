while True:
    try:
        n = input()

        ans = int(n[0])
        for i in range(1, len(n), 1):
            if i%2==0:
                ans -= int(n[i])
            else:
                ans += int(n[i])

        print(ans)
    except:
        break
