from itertools import combinations

a = int(input())
z = list(map(int, input().split(",")))
data = [ list(map(int, input().split(","))) for _ in range(a)]

for i in range(len(data)):
    a = list(combinations(data[i], 5))
    
    ans = [0,0, 0,0,0,0] # 只要2~5
    for j in a:
        kk = len( set(z) & set(j) )
        ans[kk] += 1

    print(*ans[2::], sep=",")