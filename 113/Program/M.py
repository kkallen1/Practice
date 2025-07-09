from math import isqrt

def f(n):
    for a in range( int(isqrt(n))+1 ):
        a2 = a**2
        for b in range(a, int(isqrt(n - a2))+1 ):
            b2 = b**2
            c = int(isqrt( n - a2 - b2 ))
            if a2 + b2 + c**2 == n:
                return [a, b, c]
    
    return False

for _ in range(int(input())):
    n = int(input())

    kk = f(n)
    if kk:
        kk = sorted(kk)
        print(*kk, sep=" ")
    else:
        print(-1)