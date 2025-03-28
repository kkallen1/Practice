# WA code
# 當出現次數相同，依照ASCII由大到小排列(沒有寫)

a = input()

Dict = {}
List = []
for i in a:
    Ord = ord(i)

    if i in List:
        Dict[Ord] += 1
    else:
        List.append(i)
        Dict[Ord] = 1

    ans = sorted(Dict.items(), key=lambda item: item[1])
for key, item in ans:
    print(key, item)
