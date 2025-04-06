n = int(input())

ans = 0
if n%2 != 0:
    n += 1
    ans = 0 -n//2
else:
    ans = n//2

print(ans)
