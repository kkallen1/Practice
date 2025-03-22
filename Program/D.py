n = int(input())
a = list(int(x) for x in input().split())

a = set(a)
a = sorted(list(a))
print(len(a))
print(*a)