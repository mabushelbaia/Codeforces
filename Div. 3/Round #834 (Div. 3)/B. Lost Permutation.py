import math
for _ in range(int(input())):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    MAX_ELEM = max(b)
    current_sum = sum(b)
    current_max = MAX_ELEM * (MAX_ELEM+1) / 2
    missing_numbers = current_max - current_sum
    if s - missing_numbers <= MAX_ELEM and s - missing_numbers != 0:
        print("NO")
        continue
    current_extinsion = s - missing_numbers
    NEW_MAX = current_max + current_extinsion
    k = (-1 + math.sqrt(1 + 8 * NEW_MAX)) / 2
    if math.ceil(k) == math.floor(k):
        print("YES")
    else:
        print("NO")