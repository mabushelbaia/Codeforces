import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = {arr[i-1]: i for i in range(1, n+1)}
    ans = -1
    for i in range(1, 1001):
        for j in range(1, 1001):
            if i in m.keys() and j in m.keys() and math.gcd(i, j) == 1:
                ans = max(ans, m[i]+m[j])
    print(ans)