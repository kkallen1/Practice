def f(kk):
    for i in a:
        if any(kk-i == x for x in a if x != i):
            return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(int(x) for x in input().split())
    kk = a[len(a)-1] # 目標值
    
    if f(kk):
        print("YES")
    else:
        print("NO")
        