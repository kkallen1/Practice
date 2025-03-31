Dict = {}

while True:
    try:
        key, item = map(str, input().split())
        Dict[item] = key
    except:
        break

while True:
    try:
        a = input()
        if not a:    # no input or space line
            break
        
        try:
            print(Dict[a])
        except:
            print("eh")
    except:
        break
