def bestSum(n, arr, memo={}):
    if n in memo: return memo[n]
    if n == 0: return []
    if n < 0: return None

    sum = None
    for i in arr:
        memo[n] = bestSum(n-i, arr, memo)
        if memo[n] != None:
            if sum == None or len(memo[n] + [i]) < len(sum):
                sum = memo[n] + [i]
    
    return sum

print(bestSum(12, [1, 4, 9]))