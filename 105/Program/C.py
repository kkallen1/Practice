for _ in range( int(input()) ):
    ip, netmask = map(str, input().split("/"))
    ip, netmask = list( map(int, ip.split(".")) ), list( map(int, netmask.split(".")) )
    
    AND = []
    for a, b in zip(ip, netmask):
        AND.append(a & b)
    
    for i in AND[:-1:]:
        print(i, end=".")
    print(AND[-1])