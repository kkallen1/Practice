data = list(map(str, input().split()))
z = ["+", "-", "*", "/", "^"]

stack = []
for i in data:
    if i not in z:
        stack.append(int(i))
    else:
        b = stack.pop()
        a = stack.pop()

        if i == "+":
            kk = a+b
        elif i == "-":
            kk = a-b
        elif i == "*":
            kk = a*b
        elif i == "/":
            kk = a//b
        stack.append(kk)
ans = stack.pop()
print(ans)