ONE = "one"
TWO = "two"

n = int(input())
for _ in range(n):
    a = input()
    
    if len(a)==5:
        print(3)
    else:
        o = [0]*3
        t = [0]*3
        for i in range(3):
            if a[i] == ONE[i]:
                o[i] = 1
            else:
                t[i] = 1
        ans = 1 if sum(o)>sum(t) else 2
        print(ans)
