List = []
for i in range(3):
    a = [int(x) for x in input().split()]
    List.append(a)

kk = [0, 0, 0]
kk[0], kk[1], kk[2] = sum(List[0]), sum(List[1]), sum(List[2])
S = (sum(kk))//2
kk[0], kk[1], kk[2] = S-kk[0], S-kk[1], S-kk[2]

for i in range(3):
    for j in range(3):
        if List[i][j] == 0:
            List[i][j] = kk[i]
            break


for i in List:
    print(*i)
