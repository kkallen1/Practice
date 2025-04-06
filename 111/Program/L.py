# AC code
n = int(input())

ans = 0
for i in range(1, n+1, 1):
    kk = bin(i)[2::]
    ans += kk.count("1")

print(ans)

# TLE code
kk = f""
n = int(input())
for i in range(1, n+1, 1):
    kk += f"{i:b}"

print(kk.count("1"))
