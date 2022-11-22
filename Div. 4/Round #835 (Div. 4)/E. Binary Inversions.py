for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    inversions = 0
    zeros, ones = 0, 0
    for elem in arr:
        if elem:
            ones+=1
        else:
            zeros+=1
            inversions+=ones
    increase, zeros_before, ones_before = 0, 0, 0
    for elem in arr:
        if elem:
            increase = max(increase, ones_before - (zeros - zeros_before))
            ones_before +=1
        else:
            zeros_before +=1
            increase = max(increase, -1*(ones_before - (zeros - zeros_before)))
    print(inversions + increase)