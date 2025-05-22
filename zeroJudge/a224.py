"""
zj a224
1. 非字母不列入考量
2. 重新排列後是否可為迴文
"""

while True:
    try:
        a = input().lower()
        a = "".join( filter(str.isalpha, a) )

        kk = set(a)
        L = []
        for i in kk:
            if a.count(i)%2 == 0:
                L.append(0)
            else:
                L.append(1)

        if sum(L) > 1:
            print("no...")
        else:
            print("yes !")
    except:
        break