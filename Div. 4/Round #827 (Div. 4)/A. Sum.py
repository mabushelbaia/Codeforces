for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if arr[0] + arr[1] ==  arr[2]:
        print("YES")
    elif arr[1] + arr[2] == arr[0]:
        print("YES")
    elif arr[0] + arr[2] == arr[1]:
        print("YES")
    else:
        print("NO")
        
