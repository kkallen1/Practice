# TLE code

def f(n):
    ans = []

    i = 2
    while n>1:
        if n%i==0:
            if i  not in ans:
                ans.append(i)
            n //= i
        else:
            i += 1
    
    return len(ans) if ans else 1
        

n = int(input())
while n != 0:
    print(f"{n} : {f(n)}")

    n = int(input())
