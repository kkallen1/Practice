# AC code
n = int(input())
for _ in range(n):
    L = [x for x in input().split()]
    
    Sum = 0
    for i in range(0, 20, 2):
        Sum += int( (L[i]+L[i+1]), 16)

    # 若長度>4  =>  超過 2 Byte  =>  進位的再加回來
    if Sum > 0xffff:
        Sum = Sum + Sum//0x10000
    
    # 轉為1的補數並轉回 十六進制
    print(hex(Sum^0xffff)[-4:])


# WA code
n = int(input())
for _ in range(n):
    L = [x for x in input().split()]
    
    Sum = 0
    for i in range(0, 20, 2):
        Sum += int( (L[i]+L[i+1]), 16)
    
    # 轉回 十六進制
    Sum = hex(Sum)[2::]
    
    # 若長度>4  =>  超過 2 Byte  =>  進位的再加回來
    if len(Sum)>4:
        tmp = Sum[0:len(Sum)-4]
        Sum = int(Sum[1::], 16) + int(tmp, 16)
        Sum = hex(Sum)[2::]

    Sum = bin( int(Sum, 16) )[2::] # 轉為二進制
    Sum = [1 if x=="0" else 0 for x in Sum] # 取1的補數
    Sum = "".join(str(x) for x in Sum) # 轉回字串
    Sum = int(Sum, 2) # 轉為十進制
    Sum = hex(Sum)[2::] # 轉回 十六進制
    
    if Sum != "0":
        print(Sum)
    else:
        print("0000")
