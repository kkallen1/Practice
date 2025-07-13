for _ in range(int(input())):
    a, b, c, d = map(int, input().split(","))

    y = (d - a*b) // (c - b)
    x = a - y
    print(f"{x},{y}")