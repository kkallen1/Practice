def f(L):
    a, b = L[:len(L)//2:], L[len(L)//2::]
    List = []
    for x, y in zip(a, b):
        List.append(x)
        List.append(y)
    return List

n, m = map(int, input().split())
L = [x for x in input().split()]

for _ in range(m):
    L = f(L)

print(*L)
