a, b = map(int, input().split())
ans = 0
if a>b:
    a, b = b, a
for i in range(a, b+1):
    if a==b:
        break
    if i%2 == 0:
        ans +=i

print(ans)