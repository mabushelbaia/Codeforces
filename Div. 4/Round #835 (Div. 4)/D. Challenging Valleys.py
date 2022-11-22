for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    decreasing, increasing = False, False
    ans = True
    for i in range(1, n):
        if a[i] < a[i-1]:
            decreasing = True
            ans = ans and not increasing
        elif a[i] > a[i-1]:
            increasing = True
    print("YES") if ans else print("NO")