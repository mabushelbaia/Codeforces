for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag  = False
    for elem in arr:
        if arr.count(elem) > 1:
            print("NO")
            flag = True
            break
    print("YES") if flag == False else None
