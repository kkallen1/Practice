n = int(input())

for _ in range(n):
    a = input()
    while a != a[::-1]:
        a = str( int(a) + int(a[::-1]))
    print(a)