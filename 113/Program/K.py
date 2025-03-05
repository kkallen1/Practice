def kk_round(num, kk=0):
    Bool = 0
    if num<0:
        num = abs(num)
        Bool = 1

    if kk== 0:
        return -int(num+0.5) if Bool else int(num + 0.5)
    else:
        aaa = 10 ** kk
        return -int(num * aaa+ 0.5) / aaa if Bool else int(num * aaa+ 0.5) / aaa

a = int(input())
for _ in range(a):
    a = float(input())
    a = kk_round(a, 2)
    print(f"{a:.2f}")