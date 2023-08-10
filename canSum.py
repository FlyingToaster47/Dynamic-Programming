def canSum(n, arr, memo={}):
    if n in memo: return memo[n]
    if n == 0: return True

    for i in arr:
        if n - i < 0: continue
        memo[n - i] = canSum(n - i, arr, memo)
        if memo[n - i] == True:
            return True
    return False

print(canSum(300, [7, 14]))