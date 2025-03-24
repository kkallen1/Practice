"""m932. 2. 蜜蜂觀察
"""

m, n, p = map(int, input().split())
List = []
for _ in rnage(m):
  L = list(input().split())
  List.append(L)
k = list(int, input().split())

# starting point
a, b = m-1, 0

# move rules: 0 1 2 3 4 5
r = (-1, 0, 1, 1, 0, -1) # row
c = (0, 1, 1, 0, -1, -1) # column

# move
def f(i):
  if (a+r[i]) < m:
    a += r[i]
  if (b+c[i]) < n:
    b += c[i]

for i in k:
  if i==0:
    f(i)
  elif i==1:
    f(i)
  elif i==2:
    f(i)
  elif i==3:
    f(i)
  elif i==4:
    f(i)
  elif i==5:
    f(i)
