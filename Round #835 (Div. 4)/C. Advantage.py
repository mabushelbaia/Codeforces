for _ in range(int(input())):
    n = int(input())
    strength = list(map(int, input().split()))
    copy = strength[:]
    max1 = max(copy)
    copy.remove(max1)
    max2 = max(copy)
    ans = []
    for i, elem in enumerate(strength):
        if elem == max1:
            ans.append(elem - max2)
        else:
            ans.append(elem - max1)
    print(*ans)