Dict = {
    "A":1+0*9,
    "J":1+8*9,
    "S":2+6*9,
    "B":1+1*9,
    "K":1+9*9,
    "T":2+7*9,
    "C":1+2*9,
    "L":2+0*9,
    "U":2+8*9,
    "D":1+3*9,
    "M":2+1*9,
    "V":2+9*9,
    "E":1+4*9,
    "N":2+2*9,
    "W":3+2*9,
    "F":1+5*9,
    "O":3+5*9,
    "X":3+0*9,
    "G":1+6*9,
    "P":2+3*9,
    "Y":3+1*9,
    "H":1+7*9,
    "Q":2+4*9,
    "Z":3+3*9,
    "I":3+4*9,
    "R":2+5*9,
}

a = input()
Eng = Dict[a[0]]
a = a[1::]

ans = Eng
kk = 8
for i in a:
    if kk==0:
        ans += int(i)
        continue
    ans += int(i)*kk
    kk -= 1

if int(a[1]) != 1 and int(a[1]) != 2:
    print("N")
elif ans%10 != 0:
    print("N")
else:
    print("Y")