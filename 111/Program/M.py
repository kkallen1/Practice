def f(n, data):
    if n == 0:
        return [""]
    
    for _ in range(2, n+1):
        data = ["0" + x for x in data] + ["1" + x for x in data[::-1]]

    return data

data = ["0", "1"]
n = int(input())
print(*f(n, data), sep="\n")