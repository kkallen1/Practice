from itertools import permutations

for _ in range(int(input())):
    a = list(map(int, input().split(",")))

    kk = sorted(permutations(str(a[0])))
    kk = list("".join(x) for x in kk)
    print(int(kk[ a[1]-1 ]) + int(kk[ a[2]-1 ]))
