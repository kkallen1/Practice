Dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

for _ in range( int(input()) ):
    a = input() # VXII
    a = a[::-1] # IIXV
    
    ans = 0
    kk = 0
    for i in a:
        now = Dict[i]
        if now < kk:
            ans -= now
        else:
            ans += now
        kk = now
    print(ans)