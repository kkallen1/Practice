for _ in range( int(input()) ):
    x, y, m = map(int, input().split())
    print(x**y % m)