# AC code
def f(n):
    if n%2 == 0:
        while n%2 == 0:
            n//=2

    if n%3 == 0:
        while n%3 == 0:
            n//=3

    if n%5 == 0:
        while n%5 == 0:
            n//=5
    
    return True if (n == 1) else False

n = int(input())
L = [int(x) for x in input().split()]
for i in L:
    if f(i):
        print("True")
    else:
        print("False")

# TLE code
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
    
    if 4 in ans: return False
    for i in range(2,6,1):
        try:
            ans.remove(i)
        except:
            continue
    
    return True if (len(ans)==0) else False

n = int(input())
L = [int(x) for x in input().split()]
for i in L:
    print(f(n))
