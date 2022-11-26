for i in range(int(input())):
    n = int(input())
    ans = int(n/2+0.5)
    print(ans)
    a, b = 1, 3*n
    for i in range(ans):
        print(a, b)
        a +=3
        b -= 3
    