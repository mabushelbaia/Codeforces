for _ in range(int(input())):
    s = input()
    n = len(s)
    if s == s[::-1]:
        new_string = "".join([2*c for c in s])
    else:
        new_string = s + s[::-1]
    print(new_string)