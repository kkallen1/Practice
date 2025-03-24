"""m932. 2. 蜜蜂觀察
"""

m, n, p = map(int, input().split())
List = []
for _ in range(m):
  List.append(input())
move = [int(x) for x in input().split()]

# move rules: 0 1 2 3 4 5
r = (-1, 0, 1, 1, 0, -1) # row
c = (0, 1, 1, 0, -1, -1) # column

# starting point
a, b = m-1, 0

ans = []
for i in move:
  tmp_a, tmp_b = a+r[i], b+c[i]

  if 0 <= tmp_a < m and 0 <= tmp_b < n:
    a, b = tmp_a , tmp_b

  ans.append(List[a][b])

print(*ans, sep="")
print(len(set(ans)))
