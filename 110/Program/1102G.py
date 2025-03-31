correct = [x for x in input().split()]

n = int(input())
for _ in range(n):
    a = [x for x in input().split()]
    c = correct.copy()
    g = a.copy()


    all_currect = [0] *4
    guess = [0] *4

    for i in range(4):
        if a[i] == correct[i]:
            all_currect[i] = 1

            c.remove(correct[i])
            g.remove(a[i])

    for i in range(len(g)):
        if g[i] in c:
            guess[i] = 1
            
            c.remove(g[i])
    
    print(f"{sum(all_currect)}A{sum(guess)}B")
