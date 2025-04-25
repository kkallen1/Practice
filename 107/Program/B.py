# 暴力解法

for _ in range( int(input()) ):
    List = [ [int(x) for x in input()] for _ in range(3)]

    if List[0][0] == List[1][0] == List[2][0] and List[0][0] !=0:
        print(List[0][0])
    elif List[0][1] == List[1][1] == List[2][1] and List[0][1] !=0:
        print(List[0][1])
    elif List[0][2] == List[1][2] == List[2][2] and List[0][2] !=0:
        print(List[0][2])
    
    elif List[0][0] == List[0][1] == List[0][2] and List[0][0] !=0:
        print(List[0][0])
    elif List[1][0] == List[1][1] == List[1][2] and List[1][0] !=0:
        print(List[1][0])
    elif List[2][0] == List[2][1] == List[2][2] and List[2][0] !=0:
        print(List[2][0])
    
    elif List[0][0] == List[1][1] == List[2][2] and List[0][0] !=0:
        print(List[0][0])
    elif List[0][2] == List[1][1] == List[2][0] and List[0][2] !=0:
        print(List[0][2])
    
    else:
        print(3)
