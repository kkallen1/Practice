from itertools import permutations

n = int(input())
ans = list(permutations([x for x in range(1, n+1, 1)],n))
ans = sorted(ans, reverse=True)
for i in ans:
    print(*i, sep="")
