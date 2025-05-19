# zj c462
# https://yuihuang.com/zj-c462/

k = int(input())
a = input()
List = [0 if 97<=ord(x)<=122 else 1 for x in a]

count = 1
L2 = []
for i in range(1, len(List)):
    if List[i-1] == List[i]:
        count += 1
    else:
        L2.append(count)
        count = 1
L2.append(count)

count = 0
L3 = []
for i in range(len(L2)):
    if L2[i] == k:
        count += 1
    else:
        if i-count-1 >= 0:
            if L2[i-count-1] > k:
                count += 1
        if L2[i] > k:
            count += 1
        L3.append(count)
        count = 0

if count > 0:
    if L2[i-count] > k:
        count += 1
    L3.append(count)
print(max(L3) * k)
