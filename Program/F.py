a = int(input())

ans = []

while a%2 == 0:
    ans.append(2)
    a = a//2

i = 3
while i*i <= a:
    while a%i == 0:
        ans.append(i)
        a = a//i
    i += 2

if a>2:
    ans.append(a)

print(*ans)