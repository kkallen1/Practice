Dict = {
    "-----":0,
    ".----":1,
    "..---":2,
    "...--":3,
    "....-":4,
    ".....":5,
    "-....":6,
    "--...":7,
    "---..":8,
    "----.":9
}

for _ in range( int(input()) ):
    a = input().split()
    for i in a[:-1:]:
        print(Dict[i], end="")
    print(Dict[ a[-1] ])
