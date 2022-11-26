def xorOfArray(arr, n):
 
    # Resultant variable
    xor_arr = 0
 
    # Iterating through every element in
    # the array
    for i in range(n):
 
        # Find XOR with the result
        xor_arr = xor_arr ^ arr[i]
 
    # Return the XOR
    return xor_arr
for _ in range(int(input())):
    n = int(input())
    if n%2:
        ans = [1] * n
    else:
        ans = [2] * (n-2) + [1, 3]
    print(*ans)