for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    print(abs(s))