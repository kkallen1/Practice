while True:
    try:
        a = input().split()
        
        odd = even = 0
        for i in a:
            index, num = i.split(":")
            index, num = int(index), float(num)
            
            if index%2 != 0:
                odd += num
            else:
                even += num
        
        print(f"{(odd - even):.5f}".rstrip('0').rstrip('.'))
    except:
        break
