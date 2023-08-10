def howContruct(str_, arr):
    if str_ == "": return []

    for i in arr:
        if str_[:len(i)] == i:
            if howContruct(str_.split(i)[-1], arr) != None:
                return [i] + howContruct(str_.split(i)[-1], arr)
    
    return None

print(howContruct('abcd', ["cd", "ab", "abcd"]))