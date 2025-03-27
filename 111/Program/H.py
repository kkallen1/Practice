# This a WA code

while True:
    try:
        n, a = map(str, input().split())
        n = int(n)
        List = [a[i:i+n] for i in range(0, len(a), n)]
        
        for i in range(len(List)):
            List[i] = List[i][::-1]
        print(*List, sep="")
    except:
        break
