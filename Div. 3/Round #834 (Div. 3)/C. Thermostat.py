for _ in range(int(input())):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    d1 = abs(a-l) # distance from current_temp to minimum temp
    d2 = abs(r-a) # distance from current_temp to maximum temp
    d3 = abs(b-l) # distance from target_temp to minimum temp
    d4 = abs(r-b) # distance from target_temp to maximum temp
    if a == b:
        print("0")
    elif abs(a-b) >= x:
        print("1")
    elif (d1 < x and d2 < x) or (d3 < x and d4 < x): # out of range
        print("-1")
    else:
        if d1 < x:
            if d4 >= x:
                print("2")
            else:
                print("3")
        elif d2 < x:
            if d3 >= x:
                print("2")
            else:
                print("3")
        else:
            print("2")



