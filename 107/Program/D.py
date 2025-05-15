import itertools

for _ in range( int(input()) ):
    a = list( map(int, input().split(",")) )
    kk = a[-1] -1
    a = sorted( itertools.permutations(a[1:-1:]) )
    print(*a[kk], sep="")