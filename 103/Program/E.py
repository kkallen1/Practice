data = [
    [i for i in range(1, 13+1)],  # 黑桃
    [i for i in range(14, 26+1)], # 紅桃
    [i for i in range(27, 39+1)], # 方塊
    [i for i in range(40, 52+1)]  # 梅花
]

from itertools import combinations

for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()

    score = 0

    for combo in combinations(a, 5):
        kk = 0
        # 同花順
        for now in data:
            # 確定是否全部同個花色
            if all(x in now for x in combo):
                if all(combo[x]+1 == combo[x+1] for x in range(5 - 1)):
                    score += 7
                    kk = 1
                    break
        
        if kk:
            continue

        # 四條
        if all(combo[x]+13 == combo[x+1] for x in range(5 - 1 -1)):
            score += 6
            kk = 1
            break

        if kk:
            continue

        # 葫蘆
        if all(combo[x]+13 == combo[x+1] for x in range(5 - 1 -2)):
            if 
            score += 6
            kk = 1
            break

    print(score)