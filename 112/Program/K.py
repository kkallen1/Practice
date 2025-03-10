t = int(input())
for _ in range(t):
    n = int(input())
    a = input()

    ans = []
    for i in range(n-1):
        kk = a[:i:] + a[i+2::]
        if kk not in ans:
            ans.append(kk)
    
    print(len(ans))