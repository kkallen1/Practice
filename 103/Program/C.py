for _ in range(int(input())):
    a = set(input())
    b = set(input())
    ans = list(a & b)
    ans.sort()
    if ans:
        print(*ans, sep="")
    else:
        print("N")
