n = int(input())

for _ in range(n):
    L = [int(x) for x in input().split()]
    L.sort(reverse=True)
    print(L[0], L[1])