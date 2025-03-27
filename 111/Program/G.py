n = int(input())

for _ in range(n):
    List = []
    L = ""
    for i in input():
        if i.isdigit():
            L+= i
        else:
            if L:
                List.append(L)
                L = ""
            List.append(i)
    List.append(L)
    L = ""

    # remove None, "", 0, False
    List = [x for x in List if x]
    
    ans = ""
    for i in range(0, len(List), 2):
        ans += List[i] * int(List[i+1])
    print(ans)
