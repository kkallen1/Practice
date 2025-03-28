while True:
    try:
        # g = group; a = string
        g, a = map(str, input().split())
        g = int(g)
        Len = len(a)//g
        List = [a[i:i+Len] for i in range(0, len(a), Len)]

        ans = ""
        for i in List:
            ans += i[::-1]

        print(ans)

    except ValueError:
        break
