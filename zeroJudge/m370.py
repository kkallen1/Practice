"""
APCS 2023 10月 第1題 交錯字串
zj m370

dada878: https://dada878.com/blogs/apcs-2023-10-solution
"""

# AC code
x, n = map(int, input().split())
N = list(map(int, input().split()))

a, b = 0, 0
for num in N:
    if num>x:
        a += 1
    else:
        b += 1
if a > b:
    print(a, max(N))
else:
    print(b, min(N))

# NA code
x, n = map(int, input().split())
N = list(map(int, input().split()))

N.sort()  
for i in range( len(N) ):
    if N[i] > x:
        a = i
        b = len(N) - i
        break
if a > b:
    print(a, N[0])
else:
    print(b, N[-1])
