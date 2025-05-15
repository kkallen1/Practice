# 使用內建符號
for _ in range( int(input()) ):
    ip, netmask = input().split("/")
    ip, netmask = list( map(int, ip.split(".")) ), list( map(int, netmask.split(".")) )
    print(ip, netmask)

    for i in range(3):
        print(256+(( ip[i] )|( ~netmask[i] )), end=".")
    print(256+ ( ( ip[3] )|( ~netmask[3] ) ) )

# 不使用內建符號
for _ in range( int(input()) ):
    # IP, 子網路遮罩
    a, b = input().split("/")
    
    a1 = []
    for i in a.split("."):
        kk = bin( int(i) )[2::]
        a1.append( "0"*(8-len(kk)) + kk )
    b1 = []
    for i in b.split("."):
        kk = bin( int(i) )[2::]
        b1.append( "0"*(8-len(kk)) + kk )
    
    b1 = ["".join( "0" if x=="1" else "1" for x in row ) for row in b1]
    
    ans = ""
    for a, b in zip(a1, b1):
        for i, j in zip(a, b):
            if int(i) or int(j):
                ans += "1"
            else:
                ans += "0"
        ans += "."
    
    ans = list(ans.split("."))
    ans.pop()
    ans = list( int(x, 2) for x in ans )
    print(*ans, sep=".")
