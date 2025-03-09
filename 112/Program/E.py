a = int(input())
for i in range(a//2, 1, -1):
    if a >= 2**i:
        print(2**i)
        break