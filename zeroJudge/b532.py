"""
zj b532
1. 用迴圈判斷運算符號
2. 用運算符號將 a, b 分開
3. 運算並輸出
"""

for _ in range( int(input()) ):
    data = input()

    kk = ["+", "-", "*", "/", "%"]
    for op in kk:
        if op in data:
            index = data.find(op)
            a, b = data[:index], data[index+1:]
            
            a, b = int( "".join( [x for x in a if x.isdigit()] ) ), int( "".join( [x for x in b if x.isdigit()]) )

            if op == "+":
                print(a+b)
            elif op == "-":
                print(a-b)
            elif op == "*":
                print(a*b)
            elif op == "/":
                print(a//b)
            elif op == "%":
                print(a%b)

            break
