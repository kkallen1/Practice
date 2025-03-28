def f(n):
    # 2 or 3 是質數
    if n==2 or n==3:
        return True
    # 除了 2 之外的偶數 or 小於2 都不是質數
    if n%2==0 or n<2:
        return False
    # 檢查3開始的數字，若可以被整除，則 n 不是質數
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    
    return True

N = int(input())

for _ in range(N):
    ans = []
    m, n = map(int, input().split())
    for i in range(m, n+1):
        if f(i):
           ans.append(i)

    print(*ans, sep="\n")
