# x = "b"
# y = "c"
# print(int(x, 16)+ int(y, 16))

n = int(input())

List = [x for x in input().split()]
L = []
for i in range(0, 20, 2):
    a = List[i]+List[i+1]
    a = int(a, 16)
    L.append(a)

Sum = hex(sum(L))[2::]
if len(Sum)>4:
    kk = Sum[0]
    Sum = bin(int(Sum[1::], 16) + int(kk, 16))[2::]
    
print(Sum)
