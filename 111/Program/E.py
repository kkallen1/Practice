n = int(input())
a = list(int(x) for x in input().split())

Dict = {x:a.count(x) for x in set(a)}

for i in sorted(Dict):
    print(i, Dict[i])