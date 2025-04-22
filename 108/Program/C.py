for _ in range( int(input()) ):
    a, b, n = map(int, input().split())
    n = str(n)

    ans = []
    for i in range(a, b+1):
        if n in str(i):
            ans.append(i)
    
    print(len(ans))