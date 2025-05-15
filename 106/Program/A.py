for _ in range( int(input()) ):
    a = input().split()

    ans = 0
    for i in a:
        if "s" in i.lower():
            ans += 1
    print(ans)