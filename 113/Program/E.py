n = int(input())
a = list(x for x in input().split())

d = {x:a.count(x) for x in set(a)}
kk = max(d.values())
ans = [x for x, count in d.items() if count==kk]
ans = sorted(ans)
for i in ans:
    print(i, kk)