from math import gcd

for _ in range( int(input()) ):
    data = list(map(int, input().split(",")))
    
    ans = 1
    for i in range( len(data) ):
        for j in range(i, len(data)):
            if i == j: continue
            kk = gcd(data[i], data[j])
            ans = kk if kk>ans else ans

    print(ans)
