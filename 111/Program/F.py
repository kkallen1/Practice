a = input()
b = input()

a = list(word for word in a if word not in b)

print(*a, sep="")