while True:
    try:
        a = list( input() for _ in range( int(input()) ) )
            
        kk = sorted(a, key=lambda x: int(x))
        print(*kk, sep="\n")
    except:
        break