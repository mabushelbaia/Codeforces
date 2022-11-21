for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if (a < b and b < c) or (a > b and b > c):
        print(b)
    elif (a < c and c < b) or (a > c and c > b):
        print(c)
    else:
        print(a)