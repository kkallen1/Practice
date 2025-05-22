while True:
    try:
        n = int(input())
        a = list( map(int, input().split()) )
    
        kk = sorted(a, key=lambda x: (x%10, -x))
        print(*kk)
    except:
        break