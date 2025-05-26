while True:
    a = int(input())
    if a == 0:
        break
    else:
        for i in range(1, a-1):
            if i%7 != 0:
                print(i, end=" ")
        if (a-1)%7 != 0:
            print(a-1)
