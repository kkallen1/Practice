for _ in range( int(input()) ):
    a = [x.lower() for x in input().split()]

    ans = [len(a), 0]
    for word in a:
        if "s" in word:
            ans[1] += 1

    print(*ans, sep=",")