for _ in range( int(input()) ):
    a = input()

    new_new_num = 0
    for i in range(16):
        if i%2 == 0:
            kk = str( int(a[i]) * 2 )
        else:
            kk = str( int(a[i]) )

        if len(kk)>1:
            kk = [int(x) for x in kk]
            new_new_num += sum(kk)
        else:
            new_new_num += int(kk)

    print("F" if new_new_num%10 != 0 else "T")