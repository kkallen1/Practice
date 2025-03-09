y = int(input()) + 1911
if y < 0:
    print("False")
elif (y%4==0 and y%100!=0) or (y%400==0):
    print("True")
else:
    print("False")