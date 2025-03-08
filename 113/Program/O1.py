L = input().split()
stack = []

for token in L:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  # 處理負數
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()
        
        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            if b == 0:
                print("Error: Division by zero")
                exit()
            stack.append(a // b)  # 整數除法

print(stack[0])