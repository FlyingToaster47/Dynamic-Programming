def howSum(n , arr, memo={}):
    if n in memo: return memo[n]
    if n == 0: return []
    if n < 0: return None

    for i in arr:
        memo[n] = howSum(n - i, arr, memo)
        if memo[n] != None:
            memo[n] = memo[n] + [i]
            return memo[n]

    return memo[n]

print(howSum(300, [5,3,4,7]))
