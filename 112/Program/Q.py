while int(input()):
    a = list(map(int, input().split()))
    T_cost = 0
    while len(a) > 1:
        a.sort()

        x = a.pop(0)
        y = a.pop(0)
        cost = x+y
        a.append(cost)
        
        T_cost += cost

    print(T_cost)