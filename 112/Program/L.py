t = int(input())

L = []
for i in range(t):
    a = int(input())
    L.append(a)
    L.sort()

    kk = len(L)//2-1 if len(L)%2==0 else len(L)//2

    if len(L)%2==0:
        print( (L[kk]+L[kk+1]) //2 )
    else:
        print( L[kk] )