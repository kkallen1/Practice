"""
zj d586
1. 先將字典都列出來(使用另一個程式列出)
2. 輸入分為兩種，數字、字元
3. 嘗試轉為數字，若失敗則為字元
4. 印出答案
"""

# Other Program, string to Dictionary
Dict = {}
a = "mjqhofawcpnsexdkvgtzblryui"
for i in range(26):
    Dict[i+1] = a[i]
print(Dict)

Dict = {}
a = "uzrmatifxopnhwvbslekycqjgd"
for i in range(26):
    Dict[a[i]] = i+1
print(Dict)

# AC code
Eng_Dict = {1: 'm', 2: 'j', 3: 'q', 4: 'h', 5: 'o', 6: 'f', 7: 'a', 8: 'w', 9: 'c', 10: 'p', 11: 'n', 12: 's', 13: 'e', 14: 'x', 15: 'd', 16: 'k', 17: 'v', 18: 'g', 19: 't', 20: 'z', 21: 'b', 22: 'l', 23: 'r', 24: 'y', 25: 'u', 26: 'i'}

Num_Dict = {'u': 1, 'z': 2, 'r': 3, 'm': 4, 'a': 5, 't': 6, 'i': 7, 'f': 8, 'x': 9, 'o': 10, 'p': 11, 'n': 12, 'h': 13, 'w': 14, 'v': 15, 'b': 16, 's': 17, 'l': 18, 'e': 19, 'k': 20, 'y': 21, 'c': 22, 'q': 23, 'j': 24, 'g': 25, 'd': 26}
for _ in range(int(input())):
    a = list(map(str, input().split()))
    a = a[1::]

    try:
        a[0] = int(a[0])
        
        ans = ""
        for i in a[:len(a):]:
            ans += Eng_Dict[int(i)]
    except:
        ans = 0
        for i in a:
            ans += Num_Dict[i]
    print(ans)
