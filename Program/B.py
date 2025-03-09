def f(x):
    if x=="Y":
        x = 0
    elif x=="O":
        x = 1
    elif x=="X":
        x = 2
    return x

a, b = map(str, input().split())
a, b = f(a), f(b)

if a == b:
    print(0)
elif (a==0 or a==1 or a==2) and (b+1==a or b-2==a):
    print(1)
else:
    print(2)