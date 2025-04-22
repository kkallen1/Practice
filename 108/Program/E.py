Dict = ["A", "C", "G", "T"]
for _ in range( int(input()) ):
    a, b = map(int, input().split())
    
    L = [ [x for x in input()] for __ in range(a) ]

    ans = ""
    # 一次抓每列第一個欄位的值
    """ e.g.
    L = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    output:
    (1, 4, 7)
    (2, 5, 8)
    (3, 6, 9)

    """
    for i in zip(*L):
        Count = [i.count("A"), i.count("C"), i.count("G"), i.count("T")]
        ans += Dict[ Count.index( max(Count) ) ]
    
    print(ans)