Dict = {
    "+":1,
    "-":1,
    "*":2,
    "/":2,
}

L = list(x for x in input().split())

stack = []
ans = []

for token in L:
    if token.isalnum():
        ans.append(token)
    elif token == "(":
        stack.append(token)
    elif token == ")":
        while stack and stack[-1] != "(":
            ans.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1] != "(" and Dict[token] <= Dict[stack[-1]]:
            ans.append(stack.pop())
        stack.append(token)

while stack:
    ans.append(stack.pop())

print(*ans)