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


# WA code

def f(n):
    ans = []

    if n%2 == 0:
        ans.append(2)
        while n%2 == 0:
            n//=2

    for i in range(3, n+1, 2):
        if n%i == 0:
            ans.append(i)
            while n%i == 0:
                n//=i
    
    return len(ans) if ans else 1
        

n = int(input())
while n != 0:
    print(f"{n} : {f(n)}")

    n = int(input())
