for _ in range(int(input())):
    x = input()
    s = [[] * 8] * 8
    for i in range(8):
        s[i] = list(input())
    for i in range(8):
        red = True
        for j in range(8):
            if s[i][j] != 'R':
                red = False
        if red:
            ans = 'R'
    for i in range(8):
        same = True
        for j in range(8):
            if s[j][i] != 'B':
                same = False
        if same:
            ans = 'B'
    print(ans)