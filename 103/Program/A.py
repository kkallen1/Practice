def f(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

for _ in range(int(input())):
    a, b = map(int, input().split(","))
    
    if abs(a-b) != 2:
        print("N")
    elif not f(a) or not f(b):
        print("N")
    else:
        print("Y")