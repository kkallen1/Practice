for _ in range( int(input()) ):
    _ = int(input())
    a = list( map(int, input().split(",")) )

    ans = 0
    for i in range( 1, len(a) ):
        if a[i-1] < a[i]:
            ans += (a[i] - a[i-1]) * 20
        else:
            ans += (a[i-1] - a[i]) * 10
    print(ans)