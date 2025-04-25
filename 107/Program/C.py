for _ in range( int(input()) ):
    a = int(input())
    happy = "kk"

    while happy == "kk":
        b = 0
        while a>0:
            b += (a%10) **2
            a = int(a/10)
        a = b

        if a == 1:
            happy = "T"
        if a == 4:
            happy = "F"
    print(happy)