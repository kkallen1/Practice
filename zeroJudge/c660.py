"""
zj c660
1. 全部小寫
2. 若迴圈跑到的值為空白則跳過，否則該值輸出大寫
"""

a = input()
for i in range(len(a)):
    a = a.lower()
    if a[i] != " ":
        a = a[0:i:] + a[i].upper() + a[i+1:len(a):]
    else:
        continue
    print(a)
