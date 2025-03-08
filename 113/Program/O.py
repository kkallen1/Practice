L = list(x for x in input().split())

def rem(a, b, c, kk):
    a, b = str(a), str(b)
    L.remove(a)
    L.remove(b)
    L[L.index(c)] = str(kk)

def f(i):
    if len(L) == 1:
        return
    c = L[i+2]
    try:
        c = int(c)
        f(i+1)
    except:
        a = int(L[i])
        b = int(L[i+1])
        
        if c=="+":
            kk = a+b
            rem(a, b, c, kk)
        elif c=="-":
            kk = a-b
            rem(a, b, c, kk)
        elif c=="*":
            kk = a*b
            rem(a, b, c, kk)
        elif c=="/":
            kk = a//b
            rem(a, b, c, kk)
        f(0)

f(0)
print(*L)