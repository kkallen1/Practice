def chien_round(num, chien=0):
    Bool = 0
    if num<0:
        num = abs(num)
        Bool = 1
    if chien== 0:
        return -int(num+0.5) if Bool else int(num + 0.5)
    else:
        aaa = 10 ** chien
        return -int(num * aaa+ 0.5) / aaa if Bool else int(num * aaa+ 0.5) / aaa
print(chien_round(0.325, 1))