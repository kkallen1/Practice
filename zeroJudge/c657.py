while True:
    try:
        a = input()
        n = 1
        kk = ""
        ans = 0
        
        for i in range(1, len(a)):
            if a[i-1] == a[i]:
                n += 1
                if n>ans:
                    ans = n
                    kk = a[i-1]
            else:
                n = 1
            
        print(kk, ans)
    except:
        break
