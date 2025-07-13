for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.pop(0)
    b.pop(0)
    a = set(a)
    b = set(b)

    print(len(a & b))