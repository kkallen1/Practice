def f(z=None):
    if z=="A":
        for i in a:
            if 65<ord(i)<90:
                return True
        return False
    if z=="a":
        for i in a:
            if 97<ord(i)<122:
                return True
        return False
    if z==2:
        for i in a:
            try:
                int(i)
                return True
            except:
                continue


a = input()

L = [
    "!",
    "@",
    "#",
    "$",
    "^",
    "&",
    "*",
    "(",
    ")",
    ",",
    ".",
    "?",
    "\"",
    ":",
    "{",
    "}",
    "|",
    "<",
    ">",
]

ans = 5
if len(a)<8:
    ans -= 1
if not any(char in a for char in L):
    ans -= 1
if not f(z="A"):
    ans -= 1
if not f(z="a"):
    ans -= 1
if not f(z=2):
    ans -= 1
print(ans)