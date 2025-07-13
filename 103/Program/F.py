def fa(n):
    while data[-1] < n:
        data.append(data[-2] + data[-1])

for _ in range(int(input())):
    data = [0, 1, 1, 2, 3, 5]
    n = int(input())

    fa(n)
    if n in data:
        print(f"{n}=" + "1" + "0"*(data.index(n)-2))
    else:
        data = sorted(data, reverse=True)
        data.pop()
        data.pop()
        data.pop(0)

        now = data.pop(0)
        ans = "1"
        for i in range(len(data)):
            if now + data[i] == n:
                ans += "1" + "0"*(len(data)-i-1)
                break
            elif now + data[i] > n:
                ans += "0"
                continue
            else:
                now += data[i]
                ans += "1"
        
        print(f"{n}={ans}")