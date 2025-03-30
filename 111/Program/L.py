# TLE code

kk = f""
n = int(input())
for i in range(1, n+1, 1):
    kk += f"{i:b}"

print(kk.count("1"))
