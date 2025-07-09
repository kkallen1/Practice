n, q = map(int, input().split())
data = list(input().split())
for _ in range(q):
    a, b = map(int, input().split())

    kk = len(set(data[a-1:b]))
    print(kk)