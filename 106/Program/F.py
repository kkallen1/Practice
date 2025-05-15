for _ in range( int(input()) ):
    List = list( map(int, input().split(", ")) )
    sortList = sorted(List)
    
    for num in List[:-1:]:
        print( sortList.index(num)+1, end=", " )
    print( sortList.index( List[-1] )+1 )