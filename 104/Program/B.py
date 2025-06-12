a = int(input())
z = list(map(int, input().split(",")))
data = [ list(map(int, input().split(","))) for _ in range(a)]

for i in range(len(data)):
    a = [data[i][0:5], data[i][1:6], data[i][0:4]+data[i][5:6], data[i][0:3]+data[i][4:6], data[i][0:2]+data[i][3:6], data[i][0:1]+data[i][2:6]]
    
    ans = [0,0, 0,0,0,0] # 只要2~5
    for j in a:
        kk = len( set(z) & set(j) )
        ans[kk] += 1

    print(*ans[2::], sep=",")