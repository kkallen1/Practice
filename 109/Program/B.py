n = int(input())

for _ in range(n):
    k = input()
    a, b = int(k), 0
    k = k[::-1]

    for i in range(len(k)):
        if k[i] == "4":
            a, b = ( a - 1*10**i ), ( b + 1*10**i )

    print(a, b)