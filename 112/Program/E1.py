a = int(input())

kk = 0
while 2**kk <= a:
    kk += 1

kk-=1
print(2**kk)